# Amplifier Collection: Issues

Persistent issue tracking for Amplifier sessions with dependency management and priority-based scheduling.

## What This Provides

- **issue_manager tool** - Create, list, update, and close issues with dependencies
- **issue-aware profile** - Pre-configured session with issue management enabled
- **Local storage** - Issues stored in `.amplifier/issues/` as JSONL files

## Installation

First, install Amplifier:

```bash
uv tool install git+https://github.com/microsoft/amplifier@next
```

Then add this collection:

```bash
uv tool install git+https://github.com/payneio/payne-amplifier@main#subdirectory=amplifier-collection-issues
```

## Usage

### Quick Start

Run Amplifier with the issue-aware profile:

```bash
amplifier run --profile issue-aware
```

Then interact with issues:

```
You: "Create an issue to implement user authentication"
Assistant: [Creates issue with the issue_manager tool]

You: "What can I work on?"
Assistant: [Lists ready issues with get_ready operation]

You: "Work on issue <id>"
Assistant: [Updates status to in_progress and begins work]
```

### Manual Configuration

Add the tool to your own profile:

```yaml
tools:
  - module: tool-issue
    source: git+https://github.com/payneio/payne-amplifier@main#subdirectory=amplifier-collection-issues/amplifier_collection_issues/modules/tool-issue
    config:
      data_dir: .amplifier/issues
      actor: assistant
```

## Data Storage

Issues are stored locally in your project:

```
<project-root>/
└── .amplifier/
    └── issues/
        ├── issues.jsonl          # Issue records
        ├── dependencies.jsonl    # Issue relationships
        └── events.jsonl          # Change history
```

## Issue Operations

The issue_manager tool supports:

- **create** - New issue with priority and type
- **list** - Filter by status, priority, assignee
- **get** - Show issue details
- **update** - Change status, priority, blocking notes
- **close** - Mark complete with reason
- **get_ready** - Find work with no blockers
- **get_blocked** - See blocked issues
- **add_dep** - Link issues with dependencies
- **remove_dep** - Remove dependency links

## Issue States

- **open** - Created, not yet started
- **in_progress** - Actively being worked on
- **blocked** - Waiting on dependencies
- **closed** - Completed

## Priorities

- **0** - Critical
- **1** - High
- **2** - Normal (default)
- **3** - Low
- **4** - Deferred

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
