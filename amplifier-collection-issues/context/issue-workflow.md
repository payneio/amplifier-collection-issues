# Issue Management Workflow

Core patterns for working with Beads issue tracking in Amplifier sessions.

## Lifecycle Stages

### 1. Discovery & Planning

**Before starting work:**

```bash
# See what issues exist
bd list

# Find issues ready to work on (no blockers)
bd ready

# Check specific issue details
bd show ISSUE-123
```

**Key questions:**
- Does an issue exist for this work?
- Are there dependencies or blockers?
- Is the issue clearly defined?

### 2. Claiming Work

**When starting an issue:**

```bash
# Update status to in_progress
bd update ISSUE-123 --status in_progress

# Optionally assign to yourself
bd update ISSUE-123 --assignee "YourName"
```

**Best practice:** Focus on one issue at a time. Complete it before starting another.

### 3. Active Development

**During implementation:**

```bash
# Add implementation notes
bd update ISSUE-123 --notes "Implemented using approach X because Y"

# Document discoveries
bd create --title "New issue discovered during ISSUE-123" \
  --type task \
  --description "Details..."

# Handle blockers
bd update ISSUE-123 --status blocked --notes "Blocked on: external API"
```

**Key practices:**
- Document key decisions in issue notes
- Create new issues for unexpected work
- Update status if blocked or progressing

### 4. Completion

**When work is done:**

```bash
# Close the issue with reason
bd close ISSUE-123 "Implemented feature X, tests passing"

# Check for unblocked dependent issues
bd list --status blocked
```

**Verify:**
- Implementation complete and tested
- Documentation updated if needed
- No dependent issues left blocked unnecessarily

## Common Patterns

### Pattern: Discovery During Implementation

**Scenario:** While implementing ISSUE-123, you discover missing functionality.

**Workflow:**
1. Create new issue for the discovery
2. If it blocks current work, add dependency
3. Decide: continue current work or pivot to blocker

```bash
# Create issue for discovery
NEW_ID=$(bd create --title "Missing validation logic" --type bug | grep -o '[A-Z]+-[0-9]+')

# Link as blocker if needed
bd dep add $NEW_ID ISSUE-123 --type blocks

# Either pivot or continue
bd update ISSUE-123 --status blocked --notes "Blocked on $NEW_ID"
```

### Pattern: Checking Project Status

**Scenario:** Understanding current project state.

**Workflow:**

```bash
# Overview statistics
bd stats

# What's in progress?
bd list --status in_progress

# What's blocked?
bd blocked

# What's ready to work on?
bd ready
```

### Pattern: Dependency Management

**Scenario:** Task B depends on Task A completing.

**Workflow:**

```bash
# Create dependency: A blocks B
bd dep add ISSUE-A ISSUE-B --type blocks

# Check what's blocking an issue
bd show ISSUE-B  # Shows blockers in output

# When A completes, check what gets unblocked
bd close ISSUE-A
bd blocked  # Verify ISSUE-B no longer appears
```

## Status Transitions

```
open
  ↓
  → in_progress (claimed and started)
       ↓
       → blocked (cannot proceed)
       |    ↓
       |    → in_progress (unblocked, resumed)
       ↓
       → closed (completed)
```

**Guidelines:**
- `open` → `in_progress`: When you start working
- `in_progress` → `blocked`: When you can't proceed (document why)
- `blocked` → `in_progress`: When blocker resolved
- `in_progress` → `closed`: When work complete and verified

## MCP vs CLI Commands

If beads MCP server is available, prefer MCP tools for structured data:

| Operation | MCP Tool | CLI Equivalent |
|-----------|----------|----------------|
| List issues | `mcp__plugin_beads_beads__list` | `bd list` |
| Show details | `mcp__plugin_beads_beads__show` | `bd show ISSUE-123` |
| Update status | `mcp__plugin_beads_beads__update` | `bd update ISSUE-123 --status X` |
| Close issue | `mcp__plugin_beads_beads__close` | `bd close ISSUE-123` |
| Find ready work | `mcp__plugin_beads_beads__ready` | `bd ready` |
| Show blocked | `mcp__plugin_beads_beads__blocked` | `bd blocked` |

**Advantages of MCP:**
- Returns structured JSON data
- Better error handling
- Easier to integrate with agent logic
- No need to parse command output

## Anti-Patterns to Avoid

### ❌ Claiming Multiple Issues Simultaneously

**Bad:**
```bash
bd update ISSUE-1 --status in_progress
bd update ISSUE-2 --status in_progress
bd update ISSUE-3 --status in_progress
```

**Better:** Focus on one issue, complete it, then move to next.

### ❌ Creating Issues Without Checking Duplicates

**Bad:** Create issue without looking if similar exists.

**Better:**
```bash
# Search first
bd list | grep "keyword"

# Then create if needed
bd create --title "..."
```

### ❌ Closing Without Verification

**Bad:**
```bash
bd close ISSUE-123  # No verification of completion
```

**Better:**
```bash
# Verify work complete
# Run tests
# Check dependent issues
bd close ISSUE-123 "Tests passing, feature complete"
```

### ❌ Leaving Issues Stale

**Bad:** Issue in `in_progress` for days with no updates.

**Better:** Update status/notes regularly or mark blocked with reason.

## Integration with Git Workflow

**Recommended pattern:**

```bash
# Start issue
bd update AMP-45 --status in_progress

# Create branch
git checkout -b feature/amp-45-new-feature

# Work and commit
git add .
git commit -m "feat(AMP-45): implement new feature"

# Complete issue
bd close AMP-45 "Feature implemented and tested"

# Push and PR
git push origin feature/amp-45-new-feature
```

**Key points:**
- Branch name includes issue ID
- Commit messages reference issue ID
- Close issue when work complete (not when PR merges)

## Tips for AI Agents

**When receiving user request:**
1. Check if it corresponds to an existing issue
2. If yes, update status and proceed
3. If no, decide if issue should be created
4. Document key decisions in issue notes

**During implementation:**
- Create issues for discovered work
- Update status if blocked
- Add notes for non-obvious decisions

**Before completing:**
- Verify all acceptance criteria met
- Check for dependent issues
- Close with summary of what was done
