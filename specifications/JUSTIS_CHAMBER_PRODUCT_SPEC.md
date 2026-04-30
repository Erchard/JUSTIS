# JUSTIS Chamber Product Specification

## Purpose

JUSTIS Chamber is a desktop application for observing and running sessions of the Heavenly Parliament.

The user does not control the discussion as a chat prompt. The user enters a deliberative institution: they can start a session, observe the debate, submit initiatives, and review the artifacts produced by the Parliament.

The application must make JUSTIS feel like a living moral parliament with an agentic core, while preserving the project's central discipline:

> regulation -> agenda -> deliberation -> objections -> cases -> decision -> artifacts.

## Product Names

- App: JUSTIS Chamber
- Core runtime: Parliament Engine
- Repository corpus: JUSTIS
- Agent layer: Deliberation Runtime

## Non-Chat Principle

The interface must not center on a generic "Ask AI anything" box.

The primary user actions are institutional:

- Submit Question
- Submit Objection
- Submit Case
- Submit Source
- Propose Procedure Change
- Propose Technical Task
- Propose Parliament Member
- Start Session
- Review Artifacts

The user is a citizen and observer, not the sovereign director of the agents.

## Main Screen

### Session Stage

The central area shows the live session transcript.

Each speech act should show:

- participant name;
- participant role;
- speech-act type;
- native language when available;
- operational translation;
- current state: speaking, preparing objection, supporting, hesitating, requesting clarification.

### Agenda Panel

The agenda panel shows:

- current session ID;
- current question;
- current stage;
- agenda items;
- boundaries of the session;
- expected output;
- completion criterion.

The stage model follows `specifications/SESSION_PROTOCOL_JML.yml`.

### Initiative Backlog

The backlog stores user and agent initiatives.

Supported initiative types:

- moral_question;
- objection;
- case;
- source;
- procedure_change;
- technical_task;
- member_candidate;
- repository_structure_change.

Each initiative has a status:

- submitted;
- classified;
- waiting;
- selected_for_agenda;
- under_discussion;
- accepted;
- rejected;
- deferred;
- converted_to_open_question;
- converted_to_issue.

### Decisions Panel

The decision panel shows structured results, not conversational summaries.

Minimum decision fields:

- decision_status;
- accepted_claim;
- main_objections;
- unresolved_objections;
- revision_conditions;
- files_to_update;
- artifact_status.

### Repository Changes Panel

The repository panel shows proposed file changes before they are written:

- protocols to create;
- indexes to update;
- backlog entries to add;
- cases to add;
- arguments to update;
- pull request candidate.

No canonical Code file may be changed unless the Canon-Safety rules in `specifications/PARLIAMENT_MAIN_LOOP.md` are satisfied.

## Agent Roles

### Functional Agents

These are required for the MVP:

- Moderator: keeps the session within regulation.
- Scribe: records the protocol.
- Procedure Guardian: checks `SESSION_PROTOCOL_JML.yml`.
- Backlog Clerk: classifies initiatives.
- Steelman Critic: searches for the strongest objection.
- Edge Case Advocate: demands boundary cases.
- Repository Maintainer: maps decisions to file changes.

### Persona Agents

Persona agents are optional in the MVP but central to the experience.

They represent reconstructed roles inspired by thinkers or traditions. They are not quotations and must not be presented as literal historical speech.

Required disclaimer:

> Persona-agent statements are role reconstructions inspired by historical thinkers or traditions. They are not direct quotations unless explicitly marked as direct_text with a source.

## Backlog Prioritization

The Parliament does not use FIFO order.

Each initiative may be scored by:

- moral_urgency: 1-5;
- foundational_importance: 1-5;
- dependency_blocking: 1-5;
- user_interest: 1-5;
- risk_of_confusion: 1-5;
- technical_feasibility: 1-5;
- requires_sources: true/false.

At session start, the Parliament discusses which backlog items:

- block future laws;
- reveal a contradiction in the Code;
- recur across many initiatives;
- are technically required for project growth;
- must be deferred because sources or cases are missing.

## Session Types

- moral_session;
- procedural_session;
- technical_session;
- source_review_session;
- codex_revision_session.

A session may change type only by explicit agenda revision.

## MVP Scope

The first prototype should do only this:

1. User starts a session.
2. The system reads the local JUSTIS repository.
3. The Parliament opens the session.
4. The Parliament confirms regulation and agenda.
5. The Parliament selects one backlog item.
6. Four to six agents conduct a short structured debate.
7. The system generates a protocol draft.
8. The user can save the artifact into `protocols/`.

Out of scope for MVP:

- 3D chamber;
- voice avatars;
- automatic pull requests;
- automatic Code changes;
- dozens of simultaneous persona agents;
- full source-verification automation.

## Stop Result

When a session is stopped or completed, the application must present:

1. session protocol;
2. decisions;
3. unresolved disagreements;
4. new open questions;
5. proposed file changes;
6. new backlog tasks;
7. optional pull request plan.

## Anti-Theater Rule

A completed session must create at least one structured artifact:

- protocol;
- decision;
- open question;
- case;
- objection;
- technical task;
- repository patch proposal.

If no artifact is produced, the session is marked as non_productive and cannot be treated as deliberative progress.

## Strong Objection Rule

No decision is accepted unless it passes a strong-objection round.

If no serious objection is found, the protocol must explicitly record that the Steelman Critic attempted to find one and failed, including the method used.

## Architecture

```text
Desktop App
  -> Session Orchestrator
  -> Parliament Engine
  -> Agent Runtime Adapter
       -> Cursor SDK
       -> OpenAI
       -> local model
       -> mock runtime for tests
  -> Repository Adapter
       -> read files
       -> propose patches
       -> write protocol
       -> update backlog
       -> create branch
       -> open pull request
```

The Parliament Engine is the heart of the system. Model providers are replaceable executors.

Cursor SDK is a strong first adapter candidate because it can run Cursor coding agents from TypeScript applications and stream agent events. Its role is still adapter-level: it executes agent work, but it does not define the Parliament's procedure or Canon-Safety rules. See `specifications/CURSOR_SDK_ADAPTER.md`.

## Core Domain Objects

- Session
- Agenda
- BacklogItem
- Participant
- SpeechAct
- Motion
- Objection
- CaseTest
- Decision
- Protocol
- RepositoryPatch
- ArtifactBundle

## Success Criteria

The MVP is successful when a user can:

- start a regulated Parliament session;
- watch a structured debate;
- submit at least one initiative;
- see agenda selection happen procedurally;
- receive a protocol artifact;
- review proposed repository changes before saving them.
