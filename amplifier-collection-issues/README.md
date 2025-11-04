# Amplifier Collection: Issue Management

Integrates Beads issue tracking with Amplifier for task-aware AI workflows.

## What This Collection Provides

- **Profile**: `issue-aware` - Configures session for issue management workflows
- **Context**: Issue workflow guidance and examples for AI agents
- **MCP Integration**: Automatically detects and uses beads MCP server when available

## Installation

```bash
pip install amplifier-collection-issues
```

## Usage

### Via Profile

```bash
amplifier run --profile issue-aware
```

The profile automatically:
- Configures session with issue management capabilities
- Loads relevant context for issue workflows
- Enables beads MCP tools if available

### Manual Configuration

```toml
[session]
collections = ["issues"]

[context]
include_from_collections = ["issues"]
```

## What Gets Configured

### Profile: issue-aware

- **Description**: Task management via Beads issue tracking
- **System Instructions**: Guides agents on issue workflow best practices
- **Context Files**: Loads workflow guidance and examples
- **MCP Tools**: Enables beads integration when available

### Context Files

1. **issue-workflow.md**: Core workflow patterns and best practices
2. **examples.md**: Concrete usage examples and scenarios

## Beads MCP Server

This collection works best with the beads MCP server:

```json
{
  "mcpServers": {
    "beads": {
      "command": "uvx",
      "args": ["--from", "beads-project", "beads", "mcp"]
    }
  }
}
```

The collection detects when beads is available and provides appropriate guidance.

## Issue Workflow Patterns

### Discovery & Planning
- List existing issues to understand project state
- Create issues for new work discovered
- Manage dependencies between tasks

### Active Development
- Update issue status as work progresses
- Add notes about implementation decisions
- Close issues when work completes

### Collaboration
- Use consistent status values (open, in_progress, blocked, closed)
- Document blocking conditions clearly
- Maintain dependency graph accuracy

## When to Use This Collection

**Include when:**
- Working on projects using Beads for task tracking
- Need structured issue management during development
- Want AI to help manage task lifecycle

**Skip when:**
- Project doesn't use issue tracking
- Ad-hoc exploratory work without formal tasks
- Simple one-off scripts or prototypes

## Example Workflows

### Starting New Work

```
User: "Work on issue AMP-15"

Agent (with collection):
1. Shows issue details (status, description, dependencies)
2. Checks for blockers
3. Updates status to in_progress
4. Proceeds with implementation
5. Closes issue when complete
```

### Discovery During Work

```
Agent discovers missing functionality:
1. Creates new issue describing the gap
2. Links as dependency if blocking current work
3. Continues or pivots based on priority
```

## Development

```bash
# Install in development mode
cd amplifier-collection-issues
pip install -e .

# Test collection loading
python -c "from amplifier_collection_issues import get_collection_info; print(get_collection_info())"
```

## Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft
trademarks or logos is subject to and must follow
[Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.

## License

MIT License - See LICENSE file for details
