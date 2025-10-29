# amplifier-module-tool-issue

Issue management tool module for Amplifier.

## Overview

Provides a thin wrapper over IssueManager operations, exposing issue queue management capabilities to the assistant via the tool interface.

## Installation

```bash
cd amplifier-module-tool-issue
uv pip install -e .
```

## Configuration

Add to your profile:

```yaml
tools:
  - module: tool-issue
    source: file:///path/to/amplifier-module-tool-issue

issue_manager:
  module: issue-manager
  source: file:///path/to/amplifier-module-issue-manager
```

## Operations

- `create`: Create a new issue
- `list`: List issues with optional filters
- `get`: Get a specific issue by ID
- `update`: Update an issue
- `close`: Close an issue
- `add_dependency`: Add a dependency between issues
- `get_ready`: Get issues ready to work on (no blockers)
- `get_blocked`: Get blocked issues and their blockers

## License

MIT
