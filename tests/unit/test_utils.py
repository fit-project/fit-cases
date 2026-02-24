from __future__ import annotations

import pytest

from fit_cases import utils


@pytest.mark.unit
def test_show_case_info_dialog_builds_dialog_and_executes(monkeypatch: pytest.MonkeyPatch) -> None:
    captured = {"case_info": None, "executed": 0}

    class FakeDialog:
        def __init__(self, case_info):
            captured["case_info"] = case_info

        def exec(self):
            captured["executed"] += 1

    monkeypatch.setattr(utils, "CaseFormDialog", FakeDialog)

    payload = {"id": 11, "name": "CaseX"}
    utils.show_case_info_dialog(payload)

    assert captured == {"case_info": payload, "executed": 1}
