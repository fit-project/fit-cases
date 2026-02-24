from __future__ import annotations

from pathlib import Path

import pytest

from fit_cases.model.case import Case
from fit_cases.model.db import Db


@pytest.mark.integration
def test_db_uses_resolved_sqlite_path(sqlite_db_path: Path) -> None:
    db = Db()

    assert db.engine.url.database == str(sqlite_db_path)
    assert db.session is not None


@pytest.mark.integration
def test_case_model_add_get_update_roundtrip(sqlite_db_path: Path, tmp_path: Path) -> None:
    logo1 = tmp_path / "logo1.bin"
    logo2 = tmp_path / "logo2.bin"
    logo1.write_bytes(b"logo-v1")
    logo2.write_bytes(b"logo-v2")

    model = Case()

    inserted = model.add(
        {
            "name": "CaseOne",
            "lawyer_name": "Lawyer",
            "operator": "Operator",
            "proceeding_type": 3,
            "courthouse": "Milan",
            "proceeding_number": 123,
            "notes": "Initial",
            "logo": str(logo1),
            "logo_height": "50",
            "logo_width": "auto",
        }
    )

    assert inserted.id is not None
    assert inserted.logo_bin == b"logo-v1"

    fetched = model.get_from_id(inserted.id)
    assert fetched.name == "CaseOne"
    assert fetched.proceeding_number == 123

    model.update(
        {
            "id": inserted.id,
            "name": "CaseUpdated",
            "notes": "Updated",
            "logo": str(logo2),
        }
    )

    updated = model.get_from_id(inserted.id)
    assert updated.name == "CaseUpdated"
    assert updated.notes == "Updated"
    assert updated.logo_bin == b"logo-v2"

    # If logo file does not exist, update should not overwrite existing logo_bin.
    model.update(
        {
            "id": inserted.id,
            "logo": str(tmp_path / "missing.bin"),
            "notes": "No logo overwrite",
        }
    )

    final = model.get_from_id(inserted.id)
    assert final.notes == "No logo overwrite"
    assert final.logo_bin == b"logo-v2"

    all_rows = model.get()
    assert len(all_rows) == 1
