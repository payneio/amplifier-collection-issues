# Amplifier

## Quick Mental Model (Read This First!)

### The 30-Second Version

**Amplifier = Linux Kernel Model for AI Agents**

```
┌─────────────────────────────────────────────────────────────┐
│  amplifier-core (KERNEL)                                     │
│  • Tiny, stable, boring                                      │
│  • Mechanisms ONLY (loading, coordinating, events)           │
│  • NEVER decides policy (which model, how to orchestrate)    │
│  • Changes rarely, backward compatible always                │
└─────────────────────────────────────────────────────────────┘
                             ▲
                             │ stable contracts ("studs")
                             ▼
┌─────────────────────────────────────────────────────────────┐
│  MODULES (USERSPACE)                                         │
│  • Providers: LLM backends (Anthropic, OpenAI, Azure, Ollama)│
│  • Tools: Capabilities (filesystem, bash, web, search, task) │
│  • Orchestrators: Execution loops (basic, streaming, events) │
│  • Contexts: Memory (simple, persistent)                     │
│  • Hooks: Observability (logging, redaction, approval)       │
│  • Agents: Config overlays for sub-session delegation        │
│                                                               │
│  Can be swapped, regenerated, evolved independently          │
└─────────────────────────────────────────────────────────────┘
```

**Key Principle**: "The center stays still so the edges can move fast."

### The 3-Minute Version

**1. Think "Bricks & Studs" (LEGO Model)**

- Each module = self-contained "brick" with functionality
- Interfaces = "studs" where bricks connect (stable contracts)
- Regenerate any brick independently without breaking the system
- **Prefer regeneration over editing** - rewrite module from spec, not line edits

**2. Kernel vs. Module Decision Framework**

```
┌─────────────────────────────────────────────────────────────┐
│ "Could two teams want different behavior here?"              │
│                                                               │
│  YES → MODULE (policy at edges)                              │
│  NO  → Maybe kernel (but prove with ≥2 modules first)        │
└─────────────────────────────────────────────────────────────┘
```

**3. Mount Plans = Configuration Contract**

- App layer creates **Mount Plan** (which modules to load, how to configure)
- Kernel validates and loads modules
- Pure mechanism - kernel NEVER decides which modules to use

**4. Event-First Observability**

- Everything important = canonical event (`session:start`, `provider:request`, `tool:execute`, etc.)
- Single JSONL log = source of truth
- Redaction happens BEFORE logging
- Tracing IDs everywhere (session_id, request_id, span_id)

**5. Documentation = Spec, Code = Implementation**

- Docs describe target state "as if it always worked this way"
- Code implements what docs describe
- Major changes: update ALL docs first → get approval → then code
- Prevents "context poisoning" for AI tools

## Core Architecture

### The Linux Kernel Analogy

| Linux Concept    | Amplifier Analog                 | What This Means                                         |
| ---------------- | -------------------------------- | ------------------------------------------------------- |
| Ring 0 kernel    | `amplifier-core`                 | Export mechanisms, never policy. Tiny & boring.         |
| Syscalls         | Kernel operations                | `create_session()`, `mount()`, `emit()` - few and sharp |
| Loadable drivers | Modules (providers, tools, etc.) | Compete at edges; comply with protocols                 |
| VFS mount points | Module mount points              | Each module = device at a stable path                   |
| Signals/Netlink  | Event bus / hooks                | Kernel emits lifecycle events; hooks observe            |
| /proc & dmesg    | Unified JSONL log                | One canonical structured stream                         |
| Capabilities/LSM | Approval & capability checks     | Deny-by-default, least privilege                        |
| Scheduler        | Orchestrator modules             | Swap strategies by replacing orchestrator               |
| VM/Memory        | Context manager                  | Deterministic compaction with events                    |

**Practical Use**: When design is unclear, ask "What would Linux do?"

- Scheduling? → Orchestrator module (userspace)
- Provider selection? → App layer policy
- Tool behavior? → Tool module
- Security policy? → Hook module

### System Flow

```
┌─────────────┐
│   App/CLI   │ Resolves config → Creates Mount Plan
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│  amplifier-core (Kernel)                                │
│  • Validates Mount Plan                                 │
│  • Loads modules via entry points or filesystem         │
│  • Creates Session with Coordinator                     │
│  • Emits lifecycle events                               │
└──────┬──────────────────────────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────────────────────────┐
│  Session Execution                                      │
│  Orchestrator.execute(prompt, context, providers, tools)│
│    → Provider.complete(messages)                        │
│    → Tool.execute(input)                                │
│    → Context.add/get/compact                            │
│    → Hooks observe all events                           │
└─────────────────────────────────────────────────────────┘
```

## 📡 Canonical Event Taxonomy

Emit these event names consistently:

| Event Pattern                      | When                | Data Includes             |
| ---------------------------------- | ------------------- | ------------------------- |
| `session:start/end`                | Session lifecycle   | session_id, mount plan    |
| `prompt:submit/complete`           | User interaction    | prompt, response          |
| `plan:start/end`                   | Planning phase      | plan details              |
| `provider:request/response/error`  | LLM calls           | messages, tokens, usage   |
| `tool:pre/post/error`              | Tool execution      | tool name, input, result  |
| `context:pre_compact/post_compact` | Memory compaction   | before/after token counts |
| `artifact:write/read`              | File operations     | file path, content hash   |
| `policy:violation`                 | Security/capability | what was attempted        |
| `approval:required/granted/denied` | User approvals      | action, decision          |

**Observability Schema** (JSONL):

```json
{
  "ts": "ISO8601",
  "lvl": "info|warn|error",
  "schema": {"name": "amplifier.log", "ver": "1.0.0"},
  "session_id": "uuid",
  "request_id": "uuid?",
  "span_id": "uuid?",
  "event": "provider:request",
  "component": "orchestrator",
  "module": "provider-anthropic?",
  "status": "success|error?",
  "duration_ms": 123,
  "data": {...},
  "error": {...}
}
```
