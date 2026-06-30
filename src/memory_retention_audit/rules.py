from __future__ import annotations

from memory_retention_audit.models import Rule

PROJECT_NAME = 'memory-retention-audit'
SUMMARY = 'Audit agent memory configs for retention, scope, and PII risks.'
SAMPLE_RISK = 'memory store enabled retention forever pii true scope global'
SAMPLE_CLEAN = 'memory store enabled retention 30d pii false scope tenant'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='retention-forever',
        severity='high',
        pattern='\\bretention\\s*(forever|indefinite|never expires)\\b',
        message='memory retention is unbounded',
        recommendation='Set a retention period and deletion workflow.',
    ),
    Rule(
        code='pii-memory',
        severity='medium',
        pattern='\\bpii\\s*true\\b',
        message='memory may store PII',
        recommendation='Add minimization, encryption, and review controls.',
    ),
    Rule(
        code='global-scope',
        severity='low',
        pattern='\\bscope\\s*global\\b',
        message='memory scope is global',
        recommendation='Use tenant or user isolation for memory.',
    ),
)
