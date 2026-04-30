# Cursor SDK Adapter For JUSTIS Chamber

## Status

Proposed integration note.

## Source Signal

Cursor has published a TypeScript SDK and cookbook for running Cursor agents from external applications, scripts, CI workflows, and services.

Relevant public sources:

- `https://github.com/cursor/cookbook`
- `https://cursor.com/blog/typescript-sdk`
- `https://cursor.com/changelog/sdk-release`

## Why It Matters

This is directly relevant to JUSTIS Chamber.

The original JUSTIS Chamber architecture treats model providers as replaceable executors under the Parliament Engine. Cursor SDK can become the first serious implementation candidate for:

- local coding-agent execution;
- cloud-agent execution;
- streaming agent events into the Session Stage;
- repository artifact preview;
- agent task orchestration;
- future MCP tool integration.

Cursor SDK should not become the heart of JUSTIS.

The heart remains:

- `Parliament Engine`;
- `specifications/SESSION_PROTOCOL_JML.yml`;
- `specifications/PARLIAMENT_MAIN_LOOP.md`;
- repository safety rules.

Cursor SDK is an adapter.

## Adapter Role

```text
JUSTIS Chamber
  -> Parliament Engine
  -> Agent Runtime Adapter
       -> Cursor SDK Adapter
       -> OpenAI Adapter
       -> Local Model Adapter
       -> Mock Adapter
```

## Candidate Responsibilities

The Cursor SDK Adapter may:

1. start one agent run for a functional role;
2. stream progress events into the UI;
3. pass repository context to the agent;
4. collect generated artifacts;
5. cancel a run when the session is stopped;
6. preserve conversation state when useful;
7. write only proposed patches, not canonical changes;
8. expose cloud-agent artifacts to the Repository Changes panel.

## Minimum MVP Use

The first practical experiment should be small:

1. Start a technical session.
2. Spawn one Cursor SDK agent as `repository_maintainer`.
3. Ask it to inspect the JUSTIS repository and propose a non-canonical protocol artifact.
4. Stream its events into the Session Stage.
5. Save nothing automatically.
6. Show the proposed artifact to the user for review.

This validates integration without risking the Code.

## Safety Rules

The adapter must obey:

- no direct writes to `codex/`;
- no automatic `DECISIONS.md` update;
- no automatic status promotion to `codex_done`;
- all outputs are proposals until reviewed;
- every generated artifact must record which adapter produced it;
- if using cloud runtime, the UI must clearly show that repository context may leave the local machine.

## Environment

Expected environment variable:

```text
CURSOR_API_KEY
```

The application must work without this key by falling back to a mock runtime or another configured adapter.

## Open Questions

- Should Cursor SDK agents be allowed to create branches directly?
- Should cloud-agent artifacts be treated differently from local-agent artifacts?
- How much repository context should be sent to external runtimes?
- Should persona agents use Cursor SDK, or only functional agents?
- Should MCP tools be exposed through Cursor, through JUSTIS Chamber directly, or both?
