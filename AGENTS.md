# amplifier-payne

This repo contains collections, profiles, and other components developed and used by Paul Payne to augment the Microsoft Amplifier framework.

## Collection Installation

To use the collections in this repository, install them via the amplifier CLI:

### amplifier-collection-issues

```bash
# Install the issues collection from git (--local for project-specific install)
amplifier collection add git+https://github.com/payneio/amplifier-payne@main#subdirectory=amplifier-collection-issues --local
```

Or for user-global installation:

```bash
amplifier collection add git+https://github.com/payneio/amplifier-payne@main#subdirectory=amplifier-collection-issues
```

After installation, the collection resources are available via:
- `@amplifier-collection-issues/README.md`
- `@amplifier-collection-issues/profiles/issue-aware.md`
- `@amplifier-collection-issues/context/issue-workflow.md`
- `@amplifier-collection-issues/context/examples.md`

### Verify Installation

```bash
# List installed collections
amplifier collection list

# Show collection details
amplifier collection show amplifier-collection-issues
```

## Collections

@amplifier-collection-issues/README.md
