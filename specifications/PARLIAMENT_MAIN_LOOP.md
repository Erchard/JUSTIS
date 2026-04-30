# Алгоритм Небесного парламенту (Main Loop)

Цей документ є **канонічною специфікацією процесу**: як JUSTIS переходить від відкритого питання до закону Кодексу, які артефакти обов’язкові, які стани існують і які дії **заборонені** поза процедурою.

## 0. Мета системи (що оптимізуємо)

Мета JUSTIS: поступово побудувати **короткий канонічний Кодекс** (`codex/`) із принципів, які:

- мають **простежуване обґрунтування** (протоколи + дерева аргументів + дослідження);
- витримують **сильні заперечення**, граничні кейси, аудит упереджень;
- залишаються **переглядними** через умови перегляду.

Ключова властивість: **канон (`codex/`) є похідним від процедури**, а не від автора тексту.

## 1. Сутності (Entities)

Позначення:

- `Q-XXX` — питання (аксіома/тема) в `OPEN_QUESTIONS.md`
- `D-XXX` — рішення в `DECISIONS.md`
- `Lex N` — закон у `codex/UNIVERSAL_JUSTICE_CODE.md`
- `Protocol` — файл у `protocols/`
- `ArgumentTree` — файл у `arguments/`
- `Research` — файл у `research/`

## 2. Артефакти (Artifacts) і їх роль

### 2.1. Канон (вітрина)

- `codex/UNIVERSAL_JUSTICE_CODE.md` + `codex/translations/*`
  - містить **лише** закони (Lex), коротко.

### 2.2. Майстерня (підтримка канону)

- `support/codex/STATUS_INDEX.md` — статуси Lex і пов’язані рішення
- `support/codex/JUSTIFICATION_INDEX.md` — навігація: Lex → Protocol/ArgumentTree/Research
- `support/codex/LAWS.md` — розгорнуті записи законів (JML/YAML) **тільки для вже внесених Lex**

### 2.3. Доказова база (process evidence)

- `protocols/` — повні протоколи дискусій/рішень
- `arguments/` — дерева аргументів/контраргументів
- `research/` — дослідження, збір позицій, кейсів, ризиків
- `cases/` — тестування на кейсах

## 3. Інваріанти (що ніколи не можна порушувати)

Це правила “runtime safety”.

### 3.1. Canon-Safety

1. **Не змінювати `codex/` без рішення**:
   - якщо немає рішення (запису в `DECISIONS.md`) про внесення/зміну Lex — `codex/` недоторканний.
2. **Не оголошувати `codex_done` без канону**:
   - статус `codex_done` для `Q-XXX` можливий лише якщо відповідний Lex реально є в `codex/`.
3. **Не додавати “новий закон” у `support/codex/LAWS.md`**, якщо Lex не внесений у `codex/`.

### 3.2. Traceability

Будь-який Lex мусить мати:

- Protocol (у `protocols/`)
- ArgumentTree (у `arguments/`)
- Research (у `research/`)
- Умови перегляду
- Відображення в `support/codex/JUSTIFICATION_INDEX.md`

### 3.3. Procedural Integrity

Рішення, яке використовується як підстава для канону, повинно мати:

- **повну дискусійну структуру** (`deliberatio_plena`) за `specifications/PROCEDURAL_INTEGRITY_STANDARD.md`,
- або бути явно позначеним як таким, що **потребує ратифікації** і тоді **не може** канонізувати Lex.

## 4. Стани питання (State machine для Q-XXX)

Джерело істини — `OPEN_QUESTIONS.md`. Допустимі стани:

`opened → in_research → in_session → protocol_done → argument_tree_done → codex_candidate → codex_done`

Додаткові стани:

- `blocked_by_deeper_question`
- `aporia`
- `ratification_required`

### 4.1. Умови переходів (Guard conditions)

Псевдокод:

```text
can_transition(Q, to_state) := guards_met(Q, to_state)

guards_met(Q, in_research) := exists(research/Q.md) OR active_work_started
guards_met(Q, in_session) := session_agenda_defined AND collegium_defined
guards_met(Q, protocol_done) := exists(protocols/...Q...) AND protocol_has_full_structure
guards_met(Q, argument_tree_done) := exists(arguments/...Q...) AND tree_has_objections_and_responses
guards_met(Q, codex_candidate) := protocol_done AND argument_tree_done AND candidate_formula_defined
guards_met(Q, codex_done) := exists(codex/Lex_for_Q) AND exists(DECISIONS_entry_for_codex_insertion)
```

## 5. Алгоритм сесії (Session Algorithm)

Сесія виконується як **чекліст DSL** у:

- `specifications/SESSION_PROTOCOL_JML.yml`

Це визначає обов’язкові кроки `ordo_processus`:

1. `initium` (agenda, collegium, boundaries, expected output)
2. `expositio_quaestionis`
3. `actus_membrorum` (thesis/obiectio/responsio з `respondet_ad`)
4. `probatio_obiectionum`
5. `casus_extremi` + `abusus_periculum` + `partes_affectae` + `audit_bias`
6. `decisio_vel_aporia` (формула + статус + умови + dissent note)
7. `metablocum` (якість процесу + next action)
8. `synchronizatio_registrorum` (оновити реєстри, якщо застосовно)

## 6. Main Loop (операційний цикл проекту)

Це “псевдокод” того, як проект рухається до мети.

```text
loop forever:
  Q := select_next_question(OPEN_QUESTIONS)
  if Q.status in {opened}:
     create Research(Q) and ArgumentTree(Q) stubs
     set Q.status := in_research

  if Q.status in {in_research, opened}:
     enrich Research(Q) with:
       - strong positions A/B
       - serious objections
       - edge cases
       - abuse test, affected parties, bias audit notes

  if ready_for_session(Q):
     run Session(Q) using SESSION_PROTOCOL_JML.yml checklist
     produce Protocol(Q)
     set Q.status := protocol_done

  if protocol_done(Q) and not argument_tree_done(Q):
     update ArgumentTree(Q) to reflect:
       - accepted theses
       - open objections
       - resolved objections
     set Q.status := argument_tree_done

  if protocol_done(Q) and argument_tree_done(Q):
     if decision_is_codex_ready(Q):
        set Q.status := codex_candidate
        schedule CodexInsertionSession(Q) OR ratify insertion decision
     else:
        record aporia/revisendum/blocked_by_deeper_question with conditions

  if Q.status == codex_candidate and parliament_approved_insertion(Q):
     edit codex/ (add Lex)
     update support/codex indexes
     update translations
     set Q.status := codex_done
```

### 6.1. `select_next_question`

Нормативне правило вибору:

1. P0 (аксіоми) блокують все інше → пріоритетні.
2. Якщо питання `blocked_by_deeper_question` — вибирати його “блокер”.
3. Якщо є `priority_ratification` у `protocols/RATIFICATION_REGISTER.md` і це блокує канон — ратифікувати спочатку.

## 7. Як це наближає нас до кінцевої мети (моніторинг прогресу)

Прогрес — це не “текст доданий”, а **вузол знання закріплений**.

Визначення “вузол закріплений”:

- `protocol_done`: є перевірювана дискусія (мінімум: actus + objections + responses + matrix + open objections + revision conditions).
- `argument_tree_done`: аргументи структуровані так, що заперечення не губляться.
- `codex_done`: коротка формула Lex з’єднана з доказовою базою і може бути використана як нормативний орієнтир.

## 8. “Де ми зараз” (поточна фаза проєкту)

Джерело істини: `OPEN_QUESTIONS.md` + `codex/UNIVERSAL_JUSTICE_CODE.md`.

Стан на зараз:

- `codex/` містить **Lex I–V**.
- `Q-006` має **`protocol_done`** (протокол + research + argument tree існують), але **ще не `codex_done`**.
- Наступний Main Loop крок для змісту: **довести Q-006 до `codex_candidate` через сесію внесення / рішення про внесення**, або зафіксувати, чому це поки `revisendum/aporia`.

## 9. Контрольні питання перед будь-якою дією (Agent/Contributor checklist)

Перед змінами:

1. Який `Q` або `D` я змінюю?
2. Який поточний стан (`OPEN_QUESTIONS.md`)?
3. Який очікуваний стан після зміни?
4. Які guard conditions я виконую?
5. Чи не порушую я інваріант Canon-Safety?
