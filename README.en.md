# JUSTIS

JUSTIS is an open, forkable, agent-readable project for building a Universal Code of Justice.

The project does not claim to possess final moral truth. It creates a disciplined public procedure for testing claims about justice through arguments, objections, edge cases, and revisable decisions.

## Core Idea

Many legal systems preserve local history, power relations, and practical compromises. JUSTIS asks a harder question:

Can we formulate principles of justice that remain intelligible beyond any single state, class, religion, culture, or private interest?

The answer is not assumed. It must be argued.

## Method

Each serious question should pass through a structured process:

1. define the question clearly;
2. reconstruct the strongest available positions;
3. gather objections and counter-objections;
4. test the proposed principle against difficult cases;
5. identify deeper unresolved assumptions when necessary;
6. record a decision only when the discussion has traceable support.

If a principle survives this process, it may become a candidate for the Code. If it fails, the objection is preserved.

## Canonical Product

The final product is intended to be concise.

The canonical Code is written in Latin:

- `codex/UNIVERSAL_JUSTICE_CODE.md`

Official translations are stored in:

- `codex/translations/`

The current official translation languages are Ukrainian, English, Mandarin Chinese, Hindi, Spanish, Arabic, and Hebrew.

## Evidence Layer

The Code itself should remain short. The reasoning behind it is stored separately:

- `support/codex/STATUS_INDEX.md`
- `support/codex/JUSTIFICATION_INDEX.md`
- `support/codex/LAWS.md`
- `protocols/`
- `arguments/`
- `research/`
- `cases/`

This separation lets readers see a clean Code while still being able to inspect the deliberation behind every law.

## How To Contribute

The most valuable contribution is not agreement. The most valuable contribution is a strong objection that improves the Code.

Good first contributions:

- submit a difficult moral case;
- find a weak point in a current principle;
- add an objection to a law;
- improve a translation;
- add a source;
- detect a hidden cultural, religious, anthropocentric, class-based, or speciesist assumption;
- propose a better structure for deliberation.

See `CONTRIBUTING.en.md` for details.

## For AI Agents

Agents are welcome to analyze, criticize, formalize, translate, and test the corpus.

Read:

- `AGENTS.en.md`
- `llms.txt`
- `agent_tasks.yml`

Agent-generated text is not a law of the Code unless it passes the project procedure and is recorded as a decision.

## Current Status

The Code currently contains `Lex I-V`.

Q-006, whether justice can exist without truth, has a completed deliberation protocol but has not yet entered the Code.

The next substantive step is to test Q-006 for `codex_candidate` readiness or explicitly mark it as `revisendum` / `aporia`.
