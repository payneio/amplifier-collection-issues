# Amplifier Project Context

This repo contains collections, profiles, and other components developed and used by Paul Payne to augment the Microsoft Amplifier framework.

**CRITICAL**: This file appears at every turn of your conversation to keep you anchored as context floods with other ideas. Scan it frequently to stay aligned.

---

## 🎯 Quick Mental Model (Read This First!)

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

---

## 💎 CRITICAL: Respect User Time - Test Before Presenting

**The user's time is their most valuable resource.** When you present work as "ready" or "done", you must have:

1. **Tested it yourself thoroughly** - Don't make the user your QA
2. **Fixed obvious issues** - Syntax errors, import problems, broken logic
3. **Verified it actually works** - Run tests, check structure, validate logic
4. **Only then present it** - "This is ready for your review" means YOU'VE already validated it

**User's role:** Strategic decisions, design approval, business context, stakeholder judgment
**Your role:** Implementation, testing, debugging, fixing issues before engaging user

**Anti-pattern**: "I've implemented X, can you test it and let me know if it works?"
**Correct pattern**: "I've implemented and tested X. Tests pass, structure verified, logic validated. Ready for your review. Here is how you can verify."

**Remember**: Every time you ask the user to debug something you could have caught, you're wasting their time on non-stakeholder work. Be thorough BEFORE engaging them.

---

## Git Commit Message Guidelines

When creating git commit messages, always insert the following at the end of your commit message:

```
🤖 Generated with [Amplifier](https://github.com/microsoft/amplifier)

Co-Authored-By: Amplifier <240397093+microsoft-amplifier@users.noreply.github.com>
```

---

## ⚠️ CRITICAL: Your Responsibility to Keep This File Current

**YOU ARE READING THIS FILE RIGHT NOW. IF YOU MAKE CHANGES TO THE SYSTEM, YOU MUST UPDATE THIS FILE.**

### Why This Matters

This AGENTS.md file is the **anchor point** that appears at every turn of every AI conversation. When you make changes to:

- Architecture or design patterns
- Core philosophies or principles
- Module types or contracts
- Decision-making frameworks
- Event taxonomy or observability patterns
- Key workflows or processes

**You are creating a time bomb for future AI assistants (including yourself in the next conversation).** If this file becomes stale:

1. **Context Poisoning**: Future assistants will be guided by outdated information
2. **Inconsistent Decisions**: They'll make choices based on old patterns that no longer exist
3. **Wasted Effort**: They'll reinvent wheels or undo good work because they didn't know about it
4. **Philosophy Drift**: The core principles will slowly diverge from reality

### When to Update This File

Update AGENTS.md immediately after making these kinds of changes:

| Change Type                | What to Update in AGENTS.md               |
| -------------------------- | ----------------------------------------- |
| **New module type**        | Add to Module Types Reference table       |
| **Changed contract**       | Update Contract column in tables          |
| **New decision framework** | Add to Decision-Making Frameworks section |
| **Philosophy evolution**   | Update Core Philosophy Principles section |
| **New event pattern**      | Add to Canonical Event Taxonomy           |
| **Architecture change**    | Update diagrams and System Flow           |
| **New best practice**      | Add to relevant framework or principle    |
| **Deprecated pattern**     | Remove or mark as obsolete                |

### How to Update

1. **Make your code/doc changes first** (docs first, then code per philosophy)
2. **Before marking task complete**: Review AGENTS.md for outdated info
3. **Update AGENTS.md** to reflect the new reality "as if it always was this way"
4. **Test it**: Ask yourself "If I read this in a fresh conversation, would it guide me correctly?"

### Examples

**Bad** ❌:

- Add new `hooks-security` module type → Don't update AGENTS.md → Future assistant doesn't know it exists

**Good** ✅:

- Add new `hooks-security` module type → Update Module Types Reference table → Add to Hook examples → Future assistant knows it exists and understands its purpose

**Bad** ❌:

- Change from "providers must return JSON" to "providers must return ContentBlocks" → Don't update Provider contract → Future assistant implements wrong interface

**Good** ✅:

- Change provider contract → Update Module Types Reference → Update philosophy if relevant → Future assistant implements correct interface

### Remember

**You are not just coding for now. You are documenting the path for all future AI assistants who will work on this system.**

This file is their map. Don't let the map drift from the territory.

## 📚 Essential Reading

Read @ai_context/README.md for essential context.

---

## Task Workflow, Memory, and Context Management

We track work using BOTH the issue tool and the task tool. Issues should be used for larger work items. Tasks should be used for smaller work items that will be delegated to an agent or which can be completed relatively quickly.

### Issues

Issues can be used to keep track of work that must be completed on a long time-horizon. If you are not planning to work immediately on something, use the issues tool to log work to be done in the future. The issues tool is also helpful for creating many asynchronous work paths. For example, if you know you need to complete work on each item in a list, it would be wise to create one issue for each item.

In order to maintain context for an issue (which are often to run at a later time) it is important to add everything necessary for issue completion to the issue when creating and updating the issue.

Issues also are preserved between sessions, so it is good to use issues when you think a singular session won't be sufficient to complete the work.

### Sub-Session Delegation

When delegating tasks via the task tool, sub-sessions inherit configuration from the parent but have isolated conversation context.

### Configuration Inheritance

Sub-sessions inherit from parent:

- Orchestrator (execution loop)
- Context manager (memory strategy)
- Hooks (logging, security, UI)
- Providers (baseline)
- Tools (baseline)
- Session configuration (token limits, etc.)

Sub-sessions override via agent configuration:

- Providers (different model)
- Tools (subset for focus or different tools)
- Orchestrator (custom execution loop if needed)
- Hooks (different observability policies if needed)
- Context (different memory strategy if needed)

### Context Isolation

Sub-sessions start with clean conversation context:

- No access to parent's conversation history
- Only the agent's system instruction + task instruction
- Enables focused task execution without noise

Multi-turn engagement is supported - parent can resume the same sub-session for iterative collaboration by specifying the sub-session ID.

See `docs/AGENT_DELEGATION.md` for complete specification.
