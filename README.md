# Memory Retention Audit

![Memory Retention Audit cover](assets/readme-cover.svg)

Audit agent memory configs for retention, scope, and PII risks. The idea is simple: give Memory Retention Audit the local file or fixture, get a readable result, and decide what needs attention before the next handoff.

## Memory Retention Audit catches

- `retention-forever` (high): memory retention is unbounded. Fix: Set a retention period and deletion workflow..
- `pii-memory` (medium): memory may store PII. Fix: Add minimization, encryption, and review controls..
- `global-scope` (low): memory scope is global. Fix: Use tenant or user isolation for memory..

## A normal pass

```bash
git clone https://github.com/mertefekurt/memory-retention-audit.git
cd memory-retention-audit
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
memory-retention-audit examples/sample.txt
memory-retention-audit examples/sample.txt --json
```

The input can be text, JSON, JSONL, or CSV. Use `--json` when another script needs the result instead of a Markdown report.

## A deliberately bad line

```text
memory store enabled retention forever pii true scope global
```

## Maintainer loop

```bash
ruff check .
pytest
python -m memory_retention_audit --help
```
