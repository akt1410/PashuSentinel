"""
app/models/_helpers.py — Shared default-factory helpers for ORM models.
"""
from __future__ import annotations

import uuid
from datetime import datetime, timezone


from sqlalchemy import JSON
from sqlalchemy.dialects.postgresql import JSONB

# Uses native JSONB on PostgreSQL for indexing, and falls back to standard JSON on SQLite
JSONType = JSON().with_variant(JSONB, "postgresql")


def _uuid() -> str:
    return str(uuid.uuid4())


def _now() -> datetime:
    return datetime.now(timezone.utc)
