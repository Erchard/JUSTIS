# Реєстр рішень Небесного парламенту

## Призначення

Цей документ фіксує прийняті рішення Небесного парламенту.

Протоколи містять повний хід обговорення. Реєстр рішень містить коротку навігаційну карту: що саме ухвалено, з яким статусом і де це обґрунтовано.

## Статуси

### Змістовий статус рішення

- `consensus_plenus` - повний консенсус.
- `consensus_limitatus` - обмежений консенсус.
- `consensus_practicus` - практичний консенсус.
- `aporia` - зафіксована нерозв'язана напруга.
- `revisendum` - потребує перегляду.

### Процедурна надійність

- `deliberatio_plena` - є повна дискусійна структура: виступи, заперечення, відповіді, матриця аргументів і умови перегляду.
- `deliberatio_partialis` - є часткова дискусія, але бракує повної структури перевірки.
- `summarium_provisorium` - є попереднє резюме або підсумок без повної дискусійної структури.
- `documentum_provisorium` - рішення зафіксоване в специфікації або робочому документі без окремого протоколу.
- `ratificatio_requiritur` - рішення потребує ратифікації повною дискусією.

Процедурна надійність не скасовує зміст рішення. Вона показує, наскільки добре документ підтверджує, що рішення справді пройшло парламентську дискусію.

## Рішення

| ID | Дата | Тема | Рішення | Змістовий статус | Процедурна надійність | Протокол |
| --- | --- | --- | --- | --- | --- | --- |
| D-001 | 2026-04-26 | Назва дискусійного клубу | Прийнято назву "Небесний парламент" як метафоричну назву дискусійного клубу. | consensus_limitatus | documentum_provisorium; ratificatio_requiritur | `specifications/HEAVENLY_PARLIAMENT_NAME.md` |
| D-002 | 2026-04-26 | Розширення складу парламенту | Додано всіх запропонованих кандидатів; поточний склад тоді став 41 індивідуальний член. | consensus_limitatus | summarium_provisorium; ratificatio_requiritur | `protocols/2026-04-26_heavenly-parliament-membership-expansion.md` |
| D-003 | 2026-04-26 | Архітектура Кодексу | Прийнято тришарову модель: короткий Кодекс, коментарі, дерева аргументів. | consensus_limitatus | summarium_provisorium; ratificatio_requiritur | `protocols/2026-04-26_codex_document_architecture.md` |
| D-004 | 2026-04-26 | Правило консенсусу | Закони Кодексу не ухвалюються більшістю; потрібне опрацювання суттєвих аргументів і контраргументів. Ратифіковано D-020. | consensus_plenus | deliberatio_plena | `protocols/2026-04-27_D-004_consensus-rule-ratification.md` |
| D-005 | 2026-04-26 | Justice Markup Language | Створено JML з латинськими ключами і робочою мовою для змісту. | consensus_limitatus | summarium_provisorium; ratificatio_requiritur | `protocols/2026-04-26_justice-markup-language-latin.md` |
| D-006 | 2026-04-26 | Регламент сесій | Кожна сесія починається з погодження порядку денного. | consensus_plenus | summarium_provisorium; ratificatio_requiritur | `protocols/2026-04-26_session-agenda-regulation.md` |
| D-007 | 2026-04-26 | Повернення теми в беклог | Тема може бути призупинена зі статусом `blocked_by_deeper_question`. | consensus_plenus | summarium_provisorium; ratificatio_requiritur | `protocols/2026-04-26_return-topic-to-backlog-rule.md` |
| D-008 | 2026-04-26 | Оновлення складу парламенту | Запроваджено статуси участі й якісну оцінку користі членів парламенту. | consensus_plenus | deliberatio_partialis; ratificatio_requiritur | `protocols/2026-04-26_membership-renewal-rule.md` |
| D-009 | 2026-04-26 | Оптимальна кількість | 41 член був прийнятним повним складом на той момент; для сесій формуються менші колегії. Після D-014 повний склад - 49. | consensus_plenus | deliberatio_partialis; ratificatio_requiritur | `protocols/2026-04-26_optimal-parliament-size.md` |
| D-010 | 2026-04-26 | Повна оцінка методології | Імплементувати сім покращень: джерельна надійність, голос вразливих сторін, реєстр рішень, аудит упереджень, критерій зрілості, dissent note, правило простоти. | consensus_plenus | deliberatio_partialis; ratificatio_requiritur | `protocols/2026-04-26_methodology-full-parliament-review.md` |
| D-011 | 2026-04-26 | Перша сесія | Погоджено порядок денний першої змістовної сесії: Q-001, Q-002, Q-004. Регламенти зберігаються як Markdown із JML-блоком метаданих. | consensus_plenus | summarium_provisorium; ratificatio_requiritur | `protocols/2026-04-26_session-001_initial-axioms.md` |
| D-012 | 2026-04-26 | Метаблок сесії | Кожна сесія має містити короткий метаблок для перевірки якості методу і процесу. | consensus_plenus | summarium_provisorium; ratificatio_requiritur | `protocols/2026-04-26_session-meta-review-rule.md` |
| D-013 | 2026-04-26 | Формалізація через DSL | Усе, що підвищує перевірюваність і дисципліну без втрати змісту, має бути формалізоване через JML або споріднений DSL. Ратифіковано D-022. | consensus_practicus | deliberatio_plena | `protocols/2026-04-27_D-013_dsl-formalization-ratification.md` |
| D-014 | 2026-04-26 | Друге розширення парламенту | Додано 8 нових індивідуальних членів: Хаммурапі, Ієшуа Га-Ноцрі, апостола Павла, Лейбніца, Ніла Стівенсона, Вернора Вінджа, Сью Джонсон і Девіда Чалмерса. Сенека вже був членом. "Техке" винесено як кандидат на уточнення. Поточний склад - 49 членів. | consensus_practicus | deliberatio_plena | `protocols/2026-04-26_membership-expansion-psychotherapy-futures-consciousness-religion-law.md` |
| D-015 | 2026-04-26 | Процедурна чесність | Запроваджено стандарт процедурної чесності; старі резюме-рішення позначаються як попередні й потребують ратифікації; для майбутніх рішень потрібна повна дискусійна структура. | consensus_practicus | deliberatio_plena | `protocols/2026-04-26_procedural-integrity-audit.md` |
| D-016 | 2026-04-27 | Третє розширення парламенту | Додано 11 нових індивідуальних членів: Вейкко Техке, Конфуція, Лао-цзи, Чжуан-цзи, Карла Маркса, Фрідріха Енгельса, Нельсона Манделу, Десмонда Туту, Квасі Віреду, Могобе Рамосе і Франца Фанона. Поточний склад - 60 членів. | consensus_practicus | deliberatio_plena | `protocols/2026-04-27_membership-expansion-east-africa-marx-psychoanalysis.md` |
| D-017 | 2026-04-27 | Порядок ратифікації | Першою чергою ратифікувати D-004, D-013, D-006, D-012 і D-003; після цього перейти до першої змістовної аксіоми Q-001. | consensus_practicus | deliberatio_plena | `protocols/2026-04-27_session-002_ratification-agenda.md` |
| D-018 | 2026-04-27 | Закон 1: Страждання | Перший запис Кодексу: страждання не можна ігнорувати, нормалізувати або заподіювати без достатнього виправдання. | consensus_limitatus | deliberatio_plena | `protocols/2026-04-27_Q-001_suffering-moral-significance.md` |
| D-019 | 2026-04-27 | Статус Сесії 001 | Сесію 001 визнано частково завершеною: Q-001 завершено і внесено до Кодексу; Q-002 і Q-004 перенесено в окремі наступні змістовні сесії. | consensus_practicus | deliberatio_plena | `protocols/2026-04-27_session-001-status-and-continuation.md` |
| D-020 | 2026-04-27 | Ратифікація D-004 | Ратифіковано правило консенсусу: закони Кодексу не ухвалюються більшістю; суттєві аргументи й контраргументи мають бути опрацьовані, а незнята суттєва незгода знижує або змінює статус рішення. | consensus_plenus | deliberatio_plena | `protocols/2026-04-27_D-004_consensus-rule-ratification.md` |
| D-021 | 2026-04-27 | Користь і участь | Проект визначено як інструмент моральної навігації, освіти, критики законів, міжкультурного діалогу і агент-дружнього дослідження; створено публічний пакет участі. | consensus_practicus | deliberatio_plena | `protocols/2026-04-27_project-utility-and-participation.md` |
| D-022 | 2026-04-27 | Ратифікація D-013 | Ратифіковано правило формалізації через DSL: структурні елементи дискусій, рішень, законів і дерев аргументів мають бути формалізовані, якщо це підвищує перевірюваність без втрати змісту. | consensus_practicus | deliberatio_plena | `protocols/2026-04-27_D-013_dsl-formalization-ratification.md` |

## Правило оновлення

Кожне нове рішення Небесного парламенту має бути додане до цього реєстру після створення протоколу.

Для кожного рішення потрібно вказувати два рівні:

1. змістовий статус рішення;
2. процедурну надійність протоколу.

Якщо процедурна надійність нижча за `deliberatio_plena`, рішення не можна використовувати як остаточну підставу для закону Кодексу без додаткової ратифікації.
