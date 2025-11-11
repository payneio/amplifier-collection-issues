# Amplifier collections

## Collection Installation

To use the collections in this repository, install them via the amplifier CLI:

### max-payne-collection

```bash
# Install the issues collection from git (--local for project-specific install)
amplifier collection add git+https://github.com/payneio/payne-amplifier@main#subdirectory=max-payne-collection --local
```

Or for user-global installation:

```bash
amplifier collection add git+https://github.com/payneio/payne-amplifier@main#subdirectory=max-payne-collection
```

After installation, the collection resources are available via:
- `@max-payne-collection/README.md`
- `@max-payne-collection/profiles/issue-aware.md`
- `@max-payne-collection/context/issue-workflow.md`
- `@max-payne-collection/context/examples.md`

### Verify Installation

```bash
# List installed collections
amplifier collection list

# Show collection details
amplifier collection show max-payne-collection
```

## Collections

@max-payne-collection/README.md
