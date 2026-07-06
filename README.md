<p align="center">
  <img src="assets/readme-cover.svg" alt="Memory Retention Audit cover" width="100%" />
</p>

# Memory Retention Audit

![stack](https://img.shields.io/badge/stack-Python-2563eb?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-16a34a?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-dc2626?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-7c3aed?style=flat-square)

Audit agent memory configs for retention, scope, and PII risks.

## Why it exists

Small review tasks are easy to skip when the signal lives in notes, spreadsheets, or loosely formatted exports. `memory-retention-audit` turns those checks into a repeatable command with plain findings and CI-friendly exit codes.

## Quick run

```bash
python -m pip install -e ".[dev]"
memory-retention-audit examples/sample.txt
memory-retention-audit examples/sample.txt --json --fail-on medium
```

## Rule set

| Rule | Severity | What it catches |
| --- | --- | --- |
| `retention-forever` | high | memory retention is unbounded |
| `pii-memory` | medium | memory may store PII |
| `global-scope` | low | memory scope is global |

## Input

The reader accepts plain text, JSON, JSONL, and CSV. That keeps it useful for hand-written notes, review exports, and small automation jobs.

## Sample risky input

```text
memory store enabled retention forever pii true scope global
```

## Development

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m memory_retention_audit --help
```

`cli.py` handles arguments, `core.py` reads and evaluates records, and `rules.py` keeps the Memory Retention Audit policy easy to review.
