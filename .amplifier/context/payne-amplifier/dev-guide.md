# payne-amplifier Development Guide

## Code Cleanliness

**No meta-commentary in production code**:

- Don't add "added on DATE" comments
- Don't add "vNext" or feature names
- Changelog entries go in CHANGELOG.md, not inline comments
- Code should be clean and self-documenting

## Required Sections in All Submodule/Repo README Files

**CRITICAL:** Every submodule and repo-root README.md must include:

1. **Contributing section** - Standard Microsoft CLA notice
2. **Trademarks section** - Microsoft trademark guidelines

**Template**: copy from `amplifier-dev/README.md`

**When updating README files:** Always verify these sections are present and current.

## Configuration (optional, defined by opinionated app layer)

**Use the profile-based configuration system:**

```bash
# Set your preferred profile
amplifier profile use dev

# Run Amplifier with applied profile
amplifier run --mode chat

# List available profiles
amplifier profile list
```

Profiles available: `foundation`, `base`, `dev`, `production`, `test`, `full`

See [docs/USER_ONBOARDING.md#quick-reference](docs/USER_ONBOARDING.md#quick-reference) for complete configuration documentation.

## Testing

### User-Level Verification (Run After Changes)

**CRITICAL**: Run verification tests after any changes to CLI, libraries, or toolkit collection:

```bash
# Quick verification (~6 seconds)
cd dev_verification
SKIP_GITHUB_TEST=1 ./run_all_tests.sh

# Full verification before releasing (~3 minutes)
./run_all_tests.sh
```

**What gets tested:**

- All CLI commands work (profile, session, provider, module, collection, source)
- All toolkit collection utilities work (file ops, progress, validation)
- All libraries install from GitHub
- Documentation examples are executable
- Dead code prevention (deprecated commands removed)

**When to run:**

- ✅ After changes to amplifier-app-cli code
- ✅ After changes to amplifier-profiles, amplifier-config, amplifier-collections, amplifier-module-resolution
- ✅ After toolkit collection changes (amplifier-collection-toolkit)
- ✅ Before committing documentation updates
- ✅ Before creating pull requests
- ✅ Before releases

See [dev_verification/README.md](dev_verification/README.md) for details.

### Interactive Testing

Run interactive sessions with specific profiles:

```bash
# Use the full-featured profile
amplifier run --profile full --mode chat
```

Test specific features:

- `/think` - Enable read-only plan mode
- `/tools` - List available tools
- `/status` - Show session information
