# memory-retention-audit

**Tiny Library.** Audit agent memory configs for retention, scope, and PII risks.

## API

Agent memory can become a privacy and safety risk. This CLI checks memory-store configs for missing retention and isolation controls.

## CLI

`memory-retention-audit` accepts agent memory config or design notes in text, JSON, JSONL, or CSV form.

## Examples

```bash
python -m pip install -e ".[dev]"
memory-retention-audit examples/sample.txt
memory-retention-audit examples/sample.txt --json --fail-on medium
```

## Design Notes

| Rule | Severity | Meaning |
|---|---:|---|
| `retention-forever` | high | memory retention is unbounded |
| `pii-memory` | medium | memory may store PII |
| `global-scope` | low | memory scope is global |

## License

```bash
ruff check .
pytest
python -m memory_retention_audit --help
```

License: MIT

### Example Input

```text
memory store enabled retention forever pii true scope global
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the memory-retention-audit policy surface explicit.
