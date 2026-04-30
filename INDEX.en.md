# JUSTIS Index

This is the English navigation map for the project.

## Main Route

1. `README.md`
2. `README.en.md`
3. `README.uk.md`
4. `codex/UNIVERSAL_JUSTICE_CODE.md`
5. `codex/translations/UNIVERSAL_JUSTICE_CODE.en.md`
6. `OPEN_QUESTIONS.md`
7. `DECISIONS.md`
8. `CASES.md`

## Session Procedure

The canonical repeatable session algorithm is written as DSL/JML in:

- `specifications/SESSION_PROTOCOL_JML.yml`

The human-readable source protocols are:

- `protocols/organizational/procedure/2026-04-26_session-agenda-regulation.md`
- `protocols/organizational/procedure/2026-04-27_D-006_session-regulation-ratification.md`
- `protocols/organizational/procedure/2026-04-28_session-protocol-dsl-and-native-language.md`

The overall project main loop is:

- `specifications/PARLIAMENT_MAIN_LOOP.md`

## JUSTIS Chamber

The desktop application concept and runtime model are specified in:

- `specifications/JUSTIS_CHAMBER_PRODUCT_SPEC.md`
- `specifications/PARLIAMENT_ENGINE_RUNTIME.yml`
- `specifications/CURSOR_SDK_ADAPTER.md`

## If You Want To Criticize A Law

1. Find the law in `codex/UNIVERSAL_JUSTICE_CODE.md`.
2. Check its status in `support/codex/STATUS_INDEX.md`.
3. Follow its justification through `support/codex/JUSTIFICATION_INDEX.md`.
4. Read the relevant deliberation record in `protocols/`.
5. Read the argument tree in `arguments/`.
6. Test it against cases in `cases/`.
7. Submit an objection or a pull request.

## Where Things Are

- `codex/` - final Code and official translations only.
- `support/codex/` - support indexes, terminology, translation policy, and detailed law records.
- `protocols/` - deliberation records and decisions.
- `arguments/` - argument and counterargument trees.
- `research/` - working research notes.
- `cases/` - test cases.
- `sources/` - source notes.
- `specifications/` - methodology, standards, JML, and membership records.
- `templates/` - templates for new documents.
- `tools/` - validation tools.
- `archive/` - historical or non-active materials.

## Current Laws

1. Lex I: De Dolore.
2. Lex II: De Dignitate.
3. Lex III: De Vi et Iure.
4. Lex IV: De Casibus Similibus.
5. Lex V: De Infirmitate.

## Next Substantive Question

Q-006 has `protocol_done` status. The next step is to test whether it is ready for `codex_candidate` or should remain `revisendum` / `aporia`.
