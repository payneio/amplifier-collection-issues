# Issue Workflow Examples

Concrete scenarios showing how to work with Beads in Amplifier sessions.

## Example 1: Starting Work on Existing Issue

**Scenario:** User asks to work on a specific issue.

**User Request:**
```
"Work on issue AMP-45 to add the new export feature"
```

**Agent Workflow:**

```bash
# 1. Get issue details
bd show AMP-45
```

**Output:**
```
Issue: AMP-45
Title: Add export feature
Status: open
Priority: 2
Type: feature
Description: Users should be able to export their data as JSON
Blockers: None
```

```bash
# 2. Check for blockers
bd blocked | grep AMP-45
# (empty output = no blockers)

# 3. Claim the issue
bd update AMP-45 --status in_progress

# 4. Proceed with implementation
echo "Starting implementation of export feature..."
```

**Agent Response:**
```
I'm working on AMP-45 (Add export feature). The issue is:
- Currently open with no blockers
- Requires JSON export functionality for user data

I've updated the status to in_progress. I'll implement the feature now.
```

## Example 2: Discovering New Work During Implementation

**Scenario:** While implementing, agent discovers missing validation.

**User Request:**
```
"Implement the user registration feature"
```

**Agent Workflow:**

```bash
# While implementing, discovers missing email validation

# Create issue for the discovery
bd create \
  --title "Add email validation utility" \
  --type task \
  --description "Need email format validation for registration" \
  --priority 3
```

**Output:**
```
Created: AMP-52 - Add email validation utility
```

```bash
# Link as dependency
bd dep add AMP-52 AMP-45 --type blocks

# Update current issue status
bd update AMP-45 --status blocked \
  --notes "Need email validation (AMP-52) before completing registration"
```

**Agent Response:**
```
While implementing registration, I discovered we need email validation.

I've created:
- AMP-52: Add email validation utility (blocks current work)

I've marked AMP-45 as blocked and will implement AMP-52 first, then return to registration.
```

## Example 3: Checking Project Status

**Scenario:** New session, want to understand current state.

**User Request:**
```
"What should I work on next?"
```

**Agent Workflow:**

```bash
# 1. Get overall statistics
bd stats
```

**Output:**
```
Total Issues: 24
Open: 8
In Progress: 3
Blocked: 2
Closed: 11
Ready to Work: 5
```

```bash
# 2. Check what's ready (no blockers)
bd ready
```

**Output:**
```
AMP-50: Update documentation (priority: 2)
AMP-51: Add unit tests for parser (priority: 3)
AMP-53: Refactor config loading (priority: 2)
```

```bash
# 3. Check what's in progress
bd list --status in_progress
```

**Output:**
```
AMP-45: Add export feature (in_progress)
AMP-48: Fix memory leak (in_progress)
AMP-49: Optimize database queries (in_progress)
```

**Agent Response:**
```
Project status:
- 3 issues currently in progress
- 5 issues ready to work on (no blockers)
- 2 issues blocked

Ready to work on:
1. AMP-50: Update documentation (priority 2)
2. AMP-51: Add unit tests for parser (priority 3)
3. AMP-53: Refactor config loading (priority 2)

I recommend starting with AMP-50 or AMP-53 based on priority. Which would you prefer?
```

## Example 4: Handling Blocker Resolution

**Scenario:** External blocker gets resolved, need to resume work.

**User Request:**
```
"The API documentation is now available, we can continue with AMP-47"
```

**Agent Workflow:**

```bash
# 1. Check current issue state
bd show AMP-47
```

**Output:**
```
Issue: AMP-47
Status: blocked
Notes: "Blocked on: API documentation not yet available"
```

```bash
# 2. Update status to resume
bd update AMP-47 --status in_progress \
  --notes "API docs now available, resuming implementation"

# 3. Continue implementation
echo "Resuming work on AMP-47..."
```

**Agent Response:**
```
Great! I've updated AMP-47 to in_progress and noted that the API documentation is now available. Continuing with implementation.
```

## Example 5: Completing Work

**Scenario:** Feature implementation finished, ready to close issue.

**Agent Workflow:**

```bash
# 1. Verify implementation complete
# (tests pass, feature works, documentation updated)

# 2. Check for dependent issues
bd show AMP-45 | grep -A 5 "Dependents:"
```

**Output:**
```
Dependents:
  AMP-56: Integration tests depend on this feature
```

```bash
# 3. Close the issue
bd close AMP-45 "Export feature implemented with JSON and CSV formats, tests passing"

# 4. Check if dependent issue is now unblocked
bd show AMP-56
```

**Output:**
```
Issue: AMP-56
Status: open
Blockers: (empty - unblocked by completion of AMP-45)
```

**Agent Response:**
```
✓ AMP-45 completed: Export feature implemented with JSON and CSV formats
✓ Tests passing
✓ Documentation updated

This unblocked AMP-56 (Integration tests), which is now ready to work on.
```

## Example 6: Using MCP Tools

**Scenario:** Same as Example 1, but using MCP instead of CLI.

**Agent Workflow (MCP):**

```python
# 1. Get issue details using MCP
result = mcp__plugin_beads_beads__show(issue_id="AMP-45")
```

**Response:**
```json
{
  "id": "AMP-45",
  "title": "Add export feature",
  "status": "open",
  "priority": 2,
  "type": "feature",
  "description": "Users should be able to export their data as JSON",
  "blockers": [],
  "dependencies": []
}
```

```python
# 2. Check for blockers
blocked = mcp__plugin_beads_beads__blocked()
amp_45_blocked = any(b["id"] == "AMP-45" for b in blocked["issues"])
# False - not blocked

# 3. Update status
mcp__plugin_beads_beads__update(
    issue_id="AMP-45",
    status="in_progress"
)
```

**Advantages:**
- Structured JSON responses (easier to parse)
- No need to parse CLI output
- Better error handling
- Type-safe interactions

## Example 7: Creating Issue with Full Details

**Scenario:** Need to create well-structured issue for complex work.

**Agent Workflow:**

```bash
bd create \
  --title "Implement caching layer" \
  --type feature \
  --priority 2 \
  --description "Add Redis caching to reduce database load" \
  --design "Use Redis with TTL of 5 minutes for frequently accessed data" \
  --acceptance "- Cache hit rate > 70%
- Response time improved by 50%
- Cache invalidation on updates" \
  --assignee "AI Agent"
```

**Output:**
```
Created: AMP-60 - Implement caching layer
```

**Best practice:** Include design and acceptance criteria upfront for clarity.

## Example 8: Dependency Chain Management

**Scenario:** Multiple issues with dependencies.

**Workflow:**

```bash
# Create issues
bd create --title "Database schema migration" --type task  # AMP-70
bd create --title "Update models for new schema" --type task  # AMP-71
bd create --title "Update API endpoints" --type task  # AMP-72
bd create --title "Update frontend" --type task  # AMP-73

# Create dependency chain
bd dep add AMP-70 AMP-71 --type blocks  # Schema blocks models
bd dep add AMP-71 AMP-72 --type blocks  # Models block API
bd dep add AMP-72 AMP-73 --type blocks  # API blocks frontend

# Find what's ready
bd ready
```

**Output:**
```
AMP-70: Database schema migration (no blockers)
```

**Agent Response:**
```
I've created a dependency chain for the schema migration work:

AMP-70 (schema) → AMP-71 (models) → AMP-72 (API) → AMP-73 (frontend)

Starting with AMP-70 since it has no blockers. As each completes, the next becomes available.
```

## Tips for Different Scenarios

### Quick Task (No Issue Needed)

**When:**
- Simple fix or one-liner
- Exploratory work
- No tracking required

**Action:** Just do the work, don't create issue.

### Medium Task (Create Issue)

**When:**
- Takes multiple steps
- Might be interrupted
- Want record of decision

**Action:** Create issue, update as you go.

### Complex Task (Plan with Issues)

**When:**
- Multiple subtasks
- Requires coordination
- Long-running work

**Action:** Create parent issue + subtask issues with dependencies.

**Example:**
```bash
# Create epic
bd create --title "User authentication system" --type epic  # AMP-80

# Create subtasks
bd create --title "Password hashing" --type task  # AMP-81
bd create --title "JWT token generation" --type task  # AMP-82
bd create --title "Login endpoint" --type task  # AMP-83

# Link to epic
bd dep add AMP-80 AMP-81 --type parent-child
bd dep add AMP-80 AMP-82 --type parent-child
bd dep add AMP-80 AMP-83 --type parent-child

# Create dependencies among subtasks
bd dep add AMP-81 AMP-83 --type blocks  # Need hashing before login
bd dep add AMP-82 AMP-83 --type blocks  # Need tokens before login
```

This creates clear structure for complex work.
