# The Amplifier Toolkit Collections

**Toolkit as Philosophy Exemplar** (@amplifier-collection-toolkit/):

The toolkit collection teaches building sophisticated AI tools using **metacognitive recipes** - multi-config patterns where code orchestrates thinking and specialized AI configs handle cognitive subtasks.

**What toolkit provides** (CORRECT):

- Structural utilities: `discover_files`, `ProgressReporter`, validation helpers
- Templates showing multi-config metacognitive recipe pattern
- `tutorial_analyzer` exemplar: 6 specialized configs, multi-stage orchestration

**What toolkit does NOT provide** (ANTI-PATTERNS):

- ❌ Session wrappers around `AmplifierSession` (use kernel directly!)
- ❌ Generic state management frameworks (each tool owns its state)
- ❌ LLM response parsing utilities (amplifier-core handles this)
- ❌ Single-config patterns (sophisticated tools need multiple configs!)

**The correct pattern** (multi-config metacognitive recipe):

```python
from amplifier_core import AmplifierSession
from amplifier_collection_toolkit import discover_files, ProgressReporter

# Multiple specialized configs (not one!)
ANALYZER_CONFIG = {
    "session": {"orchestrator": "loop-basic"},
    "providers": [{
        "module": "provider-anthropic",
        "source": "git+https://github.com/microsoft/amplifier-module-provider-anthropic@main",
        "config": {"model": "claude-sonnet-4-5", "temperature": 0.3}  # Analytical
    }],
}

SYNTHESIZER_CONFIG = {
    "session": {"orchestrator": "loop-streaming"},
    "providers": [{
        "module": "provider-anthropic",
        "source": "git+https://github.com/microsoft/amplifier-module-provider-anthropic@main",
        "config": {"model": "claude-opus-4-1", "temperature": 0.7}  # Creative
    }],
}

# Code orchestrates thinking across multiple configs
async def analyze_documents(root: Path):
    files = discover_files(root, "**/*.md")  # Toolkit utility
    progress = ProgressReporter(len(files), "Processing")  # Toolkit utility

    # Stage 1: Analytical config
    async with AmplifierSession(config=ANALYZER_CONFIG) as session:
        extractions = []
        for file in files:
            extraction = await session.execute(f"Extract: {file.read_text()}")
            extractions.append(extraction)
            progress.update()

    # Stage 2: Creative config
    async with AmplifierSession(config=SYNTHESIZER_CONFIG) as session:
        synthesis = await session.execute(f"Synthesize: {extractions}")

    return synthesis
```

**Key lessons**:

- **Multi-config pattern**: Each cognitive subtask (analytical, creative, evaluative) gets its own optimized config
- **Code orchestrates**: Decides which config when, manages state, controls flow
- **Structural utilities**: Toolkit provides file/progress/validation helpers, not AI wrappers
- **Use kernel directly**: AmplifierSession with specialized configs, no wrappers

See @amplifier-collection-toolkit/docs/TOOLKIT_GUIDE.md and `@amplifier-collection-toolkit/scenario-tools/tutorial-analyzer/` for complete guidance.

### Testing Philosophy

**Tests should catch real bugs, not duplicate code inspection**:

- ✅ **Write tests for**: Runtime invariants, edge cases, integration behavior, convention enforcement
- ❌ **Don't test**: Things obvious from reading code (e.g., "does constant FOO exist?", "does FOO equal 'foo'?")

**Examples**:

- Good: Test that ALL_EVENTS has no duplicates (catches copy-paste errors)
- Good: Test that all events follow namespace:action convention (catches typos)
- Bad: Test that SESSION_START constant exists (just read the code)
- Bad: Test that SESSION_START equals "session:start" (redundant with code)

**Principle**: If code inspection is faster than maintaining a test, skip the test.

### Efficient Batch Processing Pattern

When processing large numbers of files (e.g., updating 100+ documentation files), use the grep-based checklist pattern to avoid token waste:

**Pattern:**

```bash
# 1. Generate checklist in file
cat > /tmp/files_to_process.txt << 'EOF'
[ ] file1.md
[ ] file2.md
[ ] file3.md
...
[ ] file100.md
EOF

# 2. In your processing loop:
# Get next uncompleted item (cheap - doesn't read whole file)
NEXT_FILE=$(grep -m1 "^\[ \]" /tmp/files_to_process.txt | sed 's/\[ \] //')

# Process the file
# ... do work ...

# Mark complete (cheap - in-place edit)
sed -i "s/\[ \] $NEXT_FILE/[x] $NEXT_FILE/" /tmp/files_to_process.txt

# Repeat until done
```

**Benefits:**

- Saves massive tokens on large batches (100 files = 5 tokens per iteration vs 1000s)
- Clear progress tracking
- Resumable if interrupted
- No risk of forgetting files

**Use when:**

- Processing 10+ files systematically
- Each file requires similar updates
- Need clear progress visibility
- Want to avoid context drift
