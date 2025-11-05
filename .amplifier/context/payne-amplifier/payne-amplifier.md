# Working in the payne-amplifier repository

## 🏗️ Project Structure

## Development Guidelines

1. Every module is independently installable
2. Use entry points for module discovery
3. Follow the Tool/Provider/Context interfaces
4. Test modules in isolation before integration
5. Document module contracts in README.md

## Dependency Management

**IMPORTANT**: This project uses `uv` for all Python dependency management.

### Key Commands

**For single module development:**

```bash
cd amplifier-core
uv pip install -e .        # Install in editable mode
uv sync --dev              # Install with dev dependencies
```

**Adding dependencies:**

```bash
uv add package-name        # Add runtime dependency
uv add --dev pytest        # Add dev dependency
uv lock --upgrade          # Update all dependencies
```

**For cross-module development:**

```bash
# Install module A with editable link to module B
cd amplifier-core
uv pip install -e ../amplifier-module-provider-anthropic
```

**Running tests:**

```bash
uv run pytest              # Run tests with dependencies
```

### Important dependency management guidelines

- **NEVER manually edit `pyproject.toml` dependencies** - always use `uv add`
- To add dependencies: `cd` to the specific project directory and run `uv add <package>`
- This ensures proper dependency resolution and updates both `pyproject.toml` and `uv.lock`
- Each module manages its own dependencies independently
- Lock files (`uv.lock`) are committed for reproducible builds
- No workspace configuration - modules remain independent
- Use `uv pip install -e .` (not `pip install -e .`) for development installs

### Dependency Architecture: Two-Tier System

Amplifier uses a clear separation between build-time and runtime dependencies to enable GitHub installation without PyPI publication.

#### Tier 1: Core Packages (Build-Time)

Core packages (`amplifier-core`, `amplifier-app-cli`, `amplifier`) are installed via `uv tool install` and use **git URLs** in `[tool.uv.sources]`:

```toml
# amplifier-app-cli/pyproject.toml
[project]
dependencies = ["amplifier-core", "click>=8.1.0", ...]

[tool.uv.sources]
amplifier-core = { git = "https://github.com/microsoft/amplifier-core", branch = "main" }
```

**Why git URLs?** They work for both local development and GitHub installation:

```bash
# ✅ Works with git URLs
uv tool install git+https://github.com/microsoft/amplifier@next
uvx --from git+https://github.com/microsoft/amplifier@next amplifier run --profile dev "test"
```

**Avoid path dependencies** in core packages - they break GitHub installation:

```toml
# ❌ Breaks GitHub install
[tool.uv.sources]
amplifier-core = { path = "../amplifier-core", editable = true }
```

#### Tier 2: Module Packages (Runtime)

Module packages (providers, tools, hooks, orchestrators, context) follow the **peer dependency pattern**:

- **No amplifier-core dependency** in their `pyproject.toml`
- Loaded dynamically at runtime from git URLs
- Discovered via entry points: `[project.entry-points."amplifier.modules"]`

**Module sources specified in profiles:**

```yaml
# profiles/foundation.md
providers:
  - module: provider-anthropic
    source: git+https://github.com/microsoft/amplifier-module-provider-anthropic@main
    config:
      default_model: claude-sonnet-4-5
```

**Critical**: Every module in a profile **MUST include `source:`** git URL. Missing sources cause runtime failures:

```yaml
# ❌ WRONG - Missing source (module won't load)
providers:
  - module: provider-anthropic
    config:
      debug: true

# ✅ CORRECT - Include source
providers:
  - module: provider-anthropic
    source: git+https://github.com/microsoft/amplifier-module-provider-anthropic@main
    config:
      debug: true
```

**Profile inheritance gotcha**: When extending profiles and overriding sections, inherited sources are lost:

```yaml
# base.md has provider with source
providers:
  - module: provider-anthropic
    source: git+https://github.com/microsoft/amplifier-module-provider-anthropic@main

# dev.md extends base
extends: base

# ❌ WRONG - Override without source loses base's source
providers:
  - module: provider-anthropic
    config:
      debug: true  # Module fails to load!

# ✅ CORRECT - Include source when overriding
providers:
  - module: provider-anthropic
    source: git+https://github.com/microsoft/amplifier-module-provider-anthropic@main
    config:
      debug: true
```

#### Benefits

- **No PyPI needed**: Git URLs eliminate publishing requirement
- **Consistent everywhere**: Same approach for local dev and production
- **Modular loading**: Runtime loading enables on-demand module installation
- **Independent repos**: Each module evolves independently with own versioning


### Standard Workflow for Major Development

For significant features or system changes, follow this documentation-first process:

1. **Planning**: Reconnaissance → informed proposal → iterate with user on decisions needed → approved plan
2. **Documentation First**: Update ALL docs to target state ("as if it always worked this way") → scrub old references (context poison) → iterate until approved → implementation notes go in `ai_working/` only
3. **Implementation**: Code matches documentation (docs drive code) → update docs if unexpected changes needed → halt for risky decisions
4. **Test as User**: Use actual CLI/tools, verify outputs/logs match expectations → return to earlier phases if issues found
5. **Report & Cleanup**: Summary of work, verification steps for user, clean up temporary files, update task tracking → do not commit unless directed

This prevents context drift and ensures documentation remains the living specification.

### Documentation-First Retcon Technique

The non-code files for this codebase and any of its submodules is to also serve as the source of truth that is the contract the code must fulfill and align to, to support the @ai_context/@MODULAR_DESIGN_PHILOSOPHY.md approach.

In addition, AI tooling counts on these files as a key piece of its context and any conflicts or inconsistencies across the corpus is considered "context poisoning", in that it is possible the AI tooling may load stale content that misleads it into the wrong design or implementation choices and cause it to increase the divergence. For this reason, it is CRITICAL to consistently keep all non-coding files clean, up-to-date, and consistent to drive down any potential context poisoning. This is important enough that it even warrants breaking traditional best practices such as immutable ADRs in favor of "rewriting as if it were always this way" or deleting/scrubbing what is no longer relevant. Same with non-critial backwards compatability, migration, or change tracking.

For major architectural changes where documentation needs to reflect the new reality:

**Process:**

1. **Create documentation index**: Generate list of all non-code, non-git-ignored files to process
2. **Sequential processing**: Use grep-based checklist to process one file at a time
3. **Retcon updates**: Update each file to reflect future state as if it's already implemented
   - No "this will change to X" - write as if X is reality
   - No migration paths or backwards compatibility notes
   - No cruft about how things used to work
   - Just clean, current documentation of how it works
4. **Mark complete**: Update index and move to next file
5. **Report readiness**: When all docs updated, report to user for review
6. **Implement code**: After approval, treat documentation as ground truth and update code to match

**Key principle**: Documentation IS the spec. Code implements what documentation describes.

**Benefits:**

- Documentation stays authoritative (no drift between docs and code)
- Clean state (no historical baggage or migration notes)
- Clear scope (docs define exactly what needs to be implemented)
- Reviewable (user can approve design before implementation)

**Example workflow:**

```bash
# 1. Generate file index
find amplifier-dev -type f \
  \( -name "*.md" -o -name "*.yaml" -o -name "*.toml" \) \
  ! -path "*/.git/*" ! -path "*/node_modules/*" ! -path "*/__pycache__/*" \
  > /tmp/docs_to_update.txt

# 2. Process each file
NEXT=$(head -1 /tmp/docs_to_update.txt)
# Read, update, save
sed -i '1d' /tmp/docs_to_update.txt  # Remove processed file

# 3. Repeat until empty
# 4. Report readiness
# 5. Await approval
# 6. Implement code to match docs
```