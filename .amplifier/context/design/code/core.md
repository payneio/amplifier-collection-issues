## 🎨 Core Philosophy Principles

### Ruthless Simplicity

- **KISS taken to heart**: As simple as possible, but no simpler
- **Minimize abstractions**: Every layer must justify its existence
- **Start minimal, grow as needed**: Begin with simplest implementation
- **Avoid future-proofing**: Don't build for hypothetical requirements
- **Question everything**: Regularly challenge complexity
- **YAGNI(A) - You Aren't Gonna Need It (Again)**: Aggressively delete stale content, not just avoid creating it. Old docs, deprecated code, "might be useful" references - if it's not actively valuable NOW, delete it. Stale content creates context poisoning.

### Modular Design ("Bricks & Studs")

- **Stable interfaces** ("studs"): Allow independent regeneration
- **Self-contained modules** ("bricks"): Clear responsibilities
- **Regenerate, don't edit**: Rewrite entire module from spec
- **Build in parallel**: Multiple variants simultaneously
- **AI as builder, human as architect**: Specify, don't implement

### Kernel Philosophy

- **Mechanism, not policy**: Kernel provides capabilities, not decisions
- **Small, stable, boring**: Changes rarely, maintains backward compat
- **Don't break modules**: Backward compatibility is sacred
- **Policy at edges**: All decisions in modules
- **Text-first**: Human-readable, diffable, inspectable

### Implementation Philosophy

- **80/20 principle**: One working feature > multiple partial features
- **Vertical slices**: Complete end-to-end paths first
- **Fail fast and visibly**: Meaningful errors, never silent failures
- **Direct approach**: Avoid unnecessary abstractions
- **Test behavior, not implementation**: Integration > unit tests
