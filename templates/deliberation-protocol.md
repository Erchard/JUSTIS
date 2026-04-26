# Протокол дискусії: назва

```yaml
id: deliberatio.YYYY-MM-DD.topic
typus: deliberatio
status: in_disputatione
titulus: "Назва дискусії"
quaestio: "Головне питання"
agenda:
  - "Q-000"
collegium:
  - membrum: "Name"
    munus: "role"
criterium_consensus:
  omnia_argumenta_responsa: false
  objectiones_graves_responsae: false
  dissentiones_explicatae: false
```

## Дата

## Питання

## Склад колегії

## Порядок денний

## Виступи

### Виступ 1

```yaml
id: actus.001
actor: "Name"
typus: thesis
fides_fontis: reconstruction
thesis: "Коротка теза"
status: proposita
```

Текст виступу.

### Виступ 2

```yaml
id: actus.002
actor: "Name"
typus: obiectio
respondet_ad: actus.001
thesis: "Коротке заперечення"
status: aperta
```

Текст заперечення.

### Виступ 3

```yaml
id: actus.003
actor: "Name"
typus: responsio
respondet_ad: actus.002
thesis: "Коротка відповідь"
status_obiectionis: soluta / non_soluta / partialiter_soluta
```

Текст відповіді.

## Матриця аргументів

| ID | Автор | Тип | Теза | Відповідає на | Статус |
| --- | --- | --- | --- | --- | --- |

## Відкриті заперечення

| ID | Заперечення | Чому важливе | Поточний статус |
| --- | --- | --- | --- |

## Голос зацікавлених і вразливих сторін

## Аудит упереджень

## Метаблок

## Рішення

```yaml
id: decisio.YYYY-MM-DD.topic
typus: decisio
status: consensus_plenus / consensus_limitatus / consensus_practicus / aporia / revisendum
formula: "Коротке рішення"
conditiones:
  - "Умова або межа"
dissentiones:
  - actor: "Name"
    thesis: "Суть незгоди"
    cur_non_obstat: "Чому не блокує рішення"
```

## Умови перегляду

## Пов'язані документи
