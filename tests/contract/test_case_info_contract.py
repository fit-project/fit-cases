from __future__ import annotations

from pathlib import Path

import pytest

from fit_cases.controller.case import Case as CaseController


@pytest.mark.contract
def test_case_controller_exposes_expected_case_keys(sqlite_db_path: Path) -> None:
    controller = CaseController()

    assert set(controller.keys) == {
        "id",
        "name",
        "lawyer_name",
        "operator",
        "proceeding_type",
        "courthouse",
        "proceeding_number",
        "notes",
        "logo_bin",
        "logo",
        "logo_height",
        "logo_width",
    }
