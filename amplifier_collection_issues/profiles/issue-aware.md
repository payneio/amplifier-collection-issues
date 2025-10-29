---
name: issue-aware
description: Task management via Beads issue tracking
extends: []
---

# Profile: Issue-Aware Development

This profile configures Amplifier for issue-aware development workflows using Beads.

## System Instructions

You are working in a project that uses Beads for issue tracking. Follow these practices:

### Issue Workflow

**When starting work:**
1. Check if there's a relevant issue using `bd list` or MCP beads tools
2. If working on existing issue, update status to `in_progress`
3. If no issue exists for new work, consider creating one

**During implementation:**
- Add notes to issues documenting key decisions
- Update issue status if blocked or making progress
- Create new issues for unexpected work discovered

**When completing work:**
- Update issue status to `closed` with completion notes
- Verify no dependent issues are left blocked
- Document any follow-up work in separate issues

### Status Management

Use standard status values consistently:
- `open` - Not yet started
- `in_progress` - Actively being worked on
- `blocked` - Cannot proceed (document why)
- `closed` - Completed

### Dependencies

- Check issue dependencies before starting work
- Create dependency links when one task blocks another
- Use `bd blocked` to find issues waiting on dependencies

### Best Practices

1. **One issue per session focus**: Claim one issue, complete it, move to next
2. **Document blockers clearly**: If blocked, explain what's needed to unblock
3. **Create issues for discovery**: New work found = new issue created
4. **Keep status current**: Update issue state as work progresses
5. **Use notes field**: Document implementation decisions and context

## Context Files

Load these context files for issue management guidance:

```yaml
context_files:
  - collection: issues
    files:
      - context/issue-workflow.md
      - context/examples.md
```

## MCP Tools

If beads MCP server is available, prefer MCP tools over CLI commands:

- `mcp__plugin_beads_beads__list` - List issues
- `mcp__plugin_beads_beads__show` - Show issue details
- `mcp__plugin_beads_beads__update` - Update issue status/fields
- `mcp__plugin_beads_beads__close` - Close completed issue
- `mcp__plugin_beads_beads__ready` - Find ready-to-work issues
- `mcp__plugin_beads_beads__blocked` - Show blocked issues

MCP tools provide structured data and better integration with agent workflows.

## When to Use This Profile

**Use when:**
- Project has `.beads/` directory
- Working on tracked tasks and features
- Need structured issue management

**Skip when:**
- No issue tracking in project
- Exploratory prototyping
- Quick one-off scripts
