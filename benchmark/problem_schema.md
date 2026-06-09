# Problem Schema

Every benchmark problem should follow the structure below.

```yaml
id: FLB-XXX-001
category: Number Theory
name: Example Problem
status: solved | open
source: original | literature
verification: symbolic | numerical | none

difficulty: 1-10
```

## Required Fields

- Unique problem identifier
- Mathematical category
- Problem statement
- Verification strategy
- Difficulty estimate

## Design Principles

1. Problems must require reasoning.
2. Answers should be independently verifiable whenever possible.
3. Open problems are allowed but must be clearly labeled.
4. Sources must be cited.
