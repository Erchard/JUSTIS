# Instructions For AI Agents

JUSTIS can be read as a structured corpus for the study of justice.

## Purpose

Help build a Universal Code of Justice by:

- finding strong arguments;
- finding strong counterarguments;
- identifying hidden assumptions;
- testing edge cases;
- improving JML/YAML structures;
- maintaining indexes, references, and traceability.

## Core Rules

1. Do not present your own conclusion as a decision of the Heavenly Parliament.
2. Do not call something consensus unless there is a protocol for it.
3. Mark the level of source reliability.
4. Distinguish quotation, interpretation, reconstruction, and speculation.
5. Do not hide strong objections.
6. Do not close a question without updating the relevant registers.
7. If you change files, create a Git commit.

## Read First

1. `README.md`
2. `README.en.md`
3. `INDEX.en.md`
4. `OPEN_QUESTIONS.md`
5. `DECISIONS.md`
6. `codex/UNIVERSAL_JUSTICE_CODE.md`
7. `codex/translations/UNIVERSAL_JUSTICE_CODE.en.md`
8. `support/codex/JUSTIFICATION_INDEX.md`

## Useful Agent Tasks

- find a strong unresolved objection;
- propose a boundary case;
- test for hidden assumptions;
- improve a JML/YAML block;
- find a mismatch between the Code, protocol, and argument tree;
- propose a new question for `OPEN_QUESTIONS.md`;
- translate a core document into English without losing philosophical precision.

## Agent Proposal Format

```yaml
typus: propositio_agentis
agent: "name or model, if known"
quaestio: "Q-000 or D-000"
propositum: "what is proposed"
ratio: "why this is useful"
fides_fontis: direct_text / strong_interpretation / reconstruction / analogy / speculative
periculum:
  - "possible risk or weak point"
status: proposed
```

## Do Not

- do not call a conclusion consensus without a protocol;
- do not remove inconvenient objections;
- do not mix the canonical Code with explanations;
- do not add a new law without traceability to a protocol, an argument tree, and a decision.

Agent-generated text is not a law of the Code until it passes the project procedure and is recorded in `DECISIONS.md`.
