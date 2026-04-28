# Protocol: Session Algorithm DSL And Native-Language Acts

```yaml
id: deliberatio.2026-04-28.session_protocol_dsl_native_language
typus: deliberatio
status: consensus_practicus
titulus: "Session algorithm in JML and native-language parliamentary acts"
quaestio: "Should the session procedure be expressed as DSL, and should each parliamentary member speak in their native language where practical?"
agenda:
  - "D-006 session regulation"
  - "D-013 DSL formalization"
  - "native-language actus rule"
collegium:
  - membrum: "G. L. A. Hart"
    munus: "secondary rules and procedural clarity"
    lingua_materna: "en"
  - membrum: "Jurgen Habermas"
    munus: "discursive legitimacy"
    lingua_materna: "de"
  - membrum: "Confucius"
    munus: "ritual form and proper speech"
    lingua_materna: "zh"
  - membrum: "Laozi"
    munus: "warning against over-formalization"
    lingua_materna: "zh"
  - membrum: "Kwasi Wiredu"
    munus: "conceptual decolonization and translation"
    lingua_materna: "ak"
  - membrum: "Hannah Arendt"
    munus: "plurality of voices"
    lingua_materna: "de"
  - membrum: "Karl Popper"
    munus: "criticizability and error correction"
    lingua_materna: "de"
criterium_consensus:
  objectiones_graves_responsae: true
  dissentiones_explicatae: true
  exitus: "Create specifications/SESSION_PROTOCOL_JML.yml as the canonical procedural DSL."
```

## Question

The project already has a human-readable session regulation in:

- `protocols/organizational/procedure/2026-04-26_session-agenda-regulation.md`
- `protocols/organizational/procedure/2026-04-27_D-006_session-regulation-ratification.md`

The question is whether the actual repeatable algorithm of each session should be represented as DSL/JML rather than only as prose.

## Acts

```yaml
actus:
  - id: actus.001
    actor: "G. L. A. Hart"
    typus: thesis
    lingua_materna: "en"
    lingua_originalis: "en"
    textus_originalis: "A rule of recognition for sessions should be explicit enough to distinguish a conversation from a valid deliberative act."
    translatio_operativa:
      lingua: "uk"
      textus: "Правило визнання для сесій має бути достатньо явним, щоб відрізнити розмову від чинного deliberative act."
    thesis: "The session algorithm should be a formal DSL rule."
    status: accepta

  - id: actus.002
    actor: "Jurgen Habermas"
    typus: argumentum
    lingua_materna: "de"
    lingua_originalis: "de"
    textus_originalis: "Verstandigungsbedingungen mussen fur alle Beteiligten sichtbar sein."
    translatio_operativa:
      lingua: "en"
      textus: "The conditions of mutual understanding must be visible to all participants."
    thesis: "A DSL session protocol improves discursive transparency."
    status: accepta

  - id: actus.003
    actor: "Confucius"
    typus: argumentum
    lingua_materna: "zh"
    lingua_originalis: "zh-Latn"
    textus_originalis: "Li bu shi kong xingshi; li shi shi yan yu xing dong ge de qi suo."
    translatio_operativa:
      lingua: "en"
      textus: "Ritual is not empty form; it lets speech and action find their proper place."
    thesis: "A session form can discipline attention without replacing substance."
    status: accepta

  - id: actus.004
    actor: "Laozi"
    typus: obiectio
    respondet_ad: "actus.001"
    lingua_materna: "zh"
    lingua_originalis: "zh-Latn"
    textus_originalis: "Dao ke dao, fei chang dao."
    translatio_operativa:
      lingua: "en"
      textus: "The way that can be fixed as a way is not the constant way."
    thesis: "A rigid DSL may freeze the living movement of inquiry."
    status: soluta

  - id: actus.005
    actor: "Karl Popper"
    typus: responsio
    respondet_ad: "actus.004"
    lingua_materna: "de"
    lingua_originalis: "de"
    textus_originalis: "Eine Regel ist gut, wenn sie Kritik erleichtert."
    translatio_operativa:
      lingua: "en"
      textus: "A rule is good when it makes criticism easier."
    thesis: "The DSL must be revisable and must include explicit conditions for revision."
    status_obiectionis: soluta

  - id: actus.006
    actor: "Kwasi Wiredu"
    typus: obiectio
    lingua_materna: "ak"
    lingua_originalis: "en"
    textus_originalis: "If all reconstructed voices speak only in a dominant operational language, the project may smuggle conceptual dominance into its method."
    translatio_operativa:
      lingua: "uk"
      textus: "Якщо всі реконструйовані голоси говорять лише домінантною робочою мовою, метод може непомітно внести концептуальне домінування."
    thesis: "Native-language actus should be preserved where practical."
    status: accepta

  - id: actus.007
    actor: "Hannah Arendt"
    typus: argumentum
    lingua_materna: "de"
    lingua_originalis: "de"
    textus_originalis: "Pluralitat erscheint auch in der Sprache."
    translatio_operativa:
      lingua: "en"
      textus: "Plurality appears also in language."
    thesis: "Native-language records protect plurality of appearance."
    status: accepta

  - id: actus.008
    actor: "G. L. A. Hart"
    typus: distinctio
    respondet_ad: "actus.006"
    lingua_materna: "en"
    lingua_originalis: "en"
    textus_originalis: "Native language should enrich the record, but operational translation remains necessary for shared validity."
    translatio_operativa:
      lingua: "uk"
      textus: "Рідна мова має збагачувати протокол, але робочий переклад лишається необхідним для спільної чинності."
    thesis: "Every native-language actus requires an operational translation."
    status: accepta
```

## Decision

```yaml
id: decisio.2026-04-28.session_protocol_dsl_native_language
typus: decisio
status: consensus_practicus
proceduralis_fides: deliberatio_partialis
formula: "The repeatable algorithm of every session is formalized in `specifications/SESSION_PROTOCOL_JML.yml`; parliamentary acts should preserve native-language speech where practical, with operational translation required."
implementatio:
  - "Create `specifications/SESSION_PROTOCOL_JML.yml`."
  - "Add native-language fields to the session actus schema."
  - "Keep human protocols as evidence and narrative context, but use the DSL as the canonical procedural checklist."
conditiones:
  - "Native-language text must not replace operational translation."
  - "If native-language reconstruction is uncertain, mark source reliability accordingly."
  - "Translation disputes become explicit objections or translation notes."
dissentiones:
  - actor: "Laozi"
    thesis: "Any formal path can become too rigid."
    cur_non_obstat: "The DSL includes revision conditions and a deeper-question escape rule."
```

## Practical Answer

The session algorithm is now in:

- `specifications/SESSION_PROTOCOL_JML.yml`

The older human-readable sources remain important as historical and argumentative support, but the operational checklist for future sessions should be the DSL file.
