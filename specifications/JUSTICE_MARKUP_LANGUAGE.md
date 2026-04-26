# Justice Markup Language

## 1. Назва

Основна назва:

> Justice Markup Language

Скорочення:

> JML

Українська назва:

> Мова розмітки справедливості

Латинський девіз:

> Lingua Iustitiae

## 2. Призначення

JML - це внутрішня мова розмітки проекту для формального опису:

- аксіом;
- законів Кодексу справедливості;
- презумпцій;
- правил зважування;
- апорій;
- аргументів;
- контраргументів;
- граничних випадків;
- ризиків зловживання;
- умов перегляду.

JML потрібна, щоб короткий Кодекс справедливості мав прозоре й структуроване обґрунтування.

## 3. Мовний принцип

JML використовує латинські назви ключових полів і статусів як формальний канон.

Змістові значення, пояснення, аргументи й коментарі можуть писатися українською або іншою робочою мовою проекту.

Правило:

> Латина дає структурну стабільність, але не повинна затемнювати зміст.

## 4. Технічний формат

На першому етапі JML оформлюється як YAML-блок усередині Markdown або як окремий `.yml` файл.

Перевага YAML:

- легко читати людині;
- можна перевіряти автоматично в майбутньому;
- добре підходить для вкладених аргументів і контраргументів;
- не потребує створення складного парсера на старті.

## 5. Базові типи

| Значення `typus` | Сенс |
| --- | --- |
| `lex` | закон |
| `principium` | принцип |
| `axioma` | аксіома |
| `praesumptio` | презумпція |
| `regula_ponderationis` | правило зважування |
| `aporia` | апорія |
| `argumentum` | аргумент |
| `obiectio` | заперечення |

## 6. Базові статуси

| Значення `status` | Сенс |
| --- | --- |
| `consensus_plenus` | повний консенсус |
| `consensus_limitatus` | обмежений консенсус |
| `consensus_practicus` | практичний консенсус |
| `aporia` | апорія |
| `in_disputatione` | у дискусії |
| `provisorium` | попередній статус |
| `revisendum` | потребує перегляду |

## 7. Базові ключі

| Ключ | Сенс |
| --- | --- |
| `id` | унікальний ідентифікатор |
| `typus` | тип запису |
| `status` | статус |
| `titulus` | назва |
| `formula` | коротка формула |
| `principium` | розгорнутий принцип |
| `thesis` | теза |
| `argumenta` | аргументи |
| `objectiones` | заперечення |
| `responsio` | відповідь |
| `casus_extremi` | граничні випадки |
| `probatio_onus` | тягар доведення |
| `abusus_periculum` | ризик зловживання |
| `revisio_condiciones` | умови перегляду |
| `fontes` | джерела |
| `protocola` | протоколи |
| `argumenta_arbor` | дерево аргументів |
| `fides_fontis` | рівень джерельної надійності |
| `partes_affectae` | зацікавлені або вразливі сторони |
| `audit_bias` | аудит упереджень |
| `dissentiones` | зафіксовані незгоди |

## 8. Мінімальна структура закону

```yaml
id: lex.example.001
typus: lex
status: consensus_plenus
titulus: "Назва закону"
formula: "Коротка формула закону."
principium: "Розгорнутий зміст принципу."
fides_fontis: reconstruction

argumenta:
  - id: argumentum.001
    thesis: "Головний аргумент."
    fontes:
      - "Автор або джерело"
    objectiones:
      - id: obiectio.001
        thesis: "Сильне заперечення."
        responsio: "Відповідь на заперечення."

casus_extremi:
  - "Граничний випадок."

probatio_onus:
  applies_to:
    - coercitio
    - restrictio_libertatis

abusus_periculum:
  gradus: medius
  nota: "Як цим принципом можуть зловживати."

partes_affectae:
  - "Хто виграє або страждає від цього принципу?"

audit_bias:
  culturalis: "not_checked"
  religiosus: "not_checked"
  genus: "not_checked"
  classis: "not_checked"
  civilizationalis: "not_checked"
  institutionalis: "not_checked"
  technologicus: "not_checked"

dissentiones:
  - actor: "Хто не погоджується?"
    thesis: "Суть незгоди."
    cur_non_obstat: "Чому це не блокує рішення?"

revisio_condiciones:
  - "Умова перегляду."

protocola:
  - "protocols/YYYY-MM-DD_topic.md"

argumenta_arbor:
  - "arguments/laws/example.md"
```

## 9. Ступені ризику

Для `abusus_periculum.gradus` використовуються:

- `humilis` - низький;
- `medius` - середній;
- `altus` - високий;
- `extremus` - крайній.

## 10. Попередній словник дій і ризиків

| Ключ | Значення |
| --- | --- |
| `coercitio` | примус |
| `restrictio_libertatis` | обмеження свободи |
| `humiliatio` | приниження |
| `violentia` | насильство |
| `mendacium` | брехня |
| `poena` | покарання |
| `expropriatio` | вилучення майна |
| `sacrificium_innocentis` | жертва невинного |
| `discriminatio` | дискримінація |
| `dominium_culturale` | культурне домінування |
| `periculum_irreversibile` | незворотний ризик |

## 11. Рівні джерельної надійності

Для `fides_fontis` використовуються:

- `direct_text` - теза прямо спирається на текст автора;
- `strong_interpretation` - сильна інтерпретація на основі текстів;
- `reconstruction` - реконструкція можливої позиції;
- `analogy` - аналогія з ширшою традицією;
- `speculative` - гіпотетичне припущення.

## 12. Правило розвитку JML

JML є експериментальною.

Вона має розвиватися через практичне використання:

1. Створити 1-2 приклади для базових аксіом.
2. Перевірити, чи структура не надто важка.
3. Уточнити словник.
4. Лише потім думати про автоматичну перевірку.

## 13. Статус

Статус JML:

> Експериментальна специфікація з обмеженим консенсусом.

JML може бути переглянута після перших практичних прикладів.
