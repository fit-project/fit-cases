from __future__ import annotations

from types import SimpleNamespace

import pytest

from fit_cases.controller import case as case_controller_module


class _FakeColumns:
    def keys(self):
        return ["id", "name", "operator"]


class _FakeModel:
    def __init__(self):
        self.metadata = SimpleNamespace(
            tables={"cases": SimpleNamespace(columns=_FakeColumns())}
        )
        self._rows = [SimpleNamespace(id=1, name="Case_A", operator="alice", db="x")]
        self.updated_payload = None

    def get(self):
        return self._rows

    def update(self, case_info):
        self.updated_payload = case_info
        self._rows = [SimpleNamespace(id=case_info["id"], name=case_info["name"], operator=case_info["operator"], db="x")]

    def add(self, case_info):
        new_row = SimpleNamespace(
            id=2,
            name=case_info["name"],
            operator=case_info["operator"],
            db="x",
        )
        self._rows.append(new_row)
        return new_row


@pytest.mark.unit
def test_controller_loads_cases_names_and_keys(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(case_controller_module, "CaseModel", _FakeModel)

    controller = case_controller_module.Case()

    assert controller.keys == ["id", "name", "operator"]
    assert controller.cases == [{"id": 1, "name": "Case_A", "operator": "alice"}]
    assert controller.names == ["Case_A"]


@pytest.mark.unit
def test_controller_cases_setter_updates_and_reloads(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(case_controller_module, "CaseModel", _FakeModel)

    controller = case_controller_module.Case()
    controller.cases = {"id": 1, "name": "Case_B", "operator": "bob"}

    assert controller.model.updated_payload == {"id": 1, "name": "Case_B", "operator": "bob"}
    assert controller.cases == [{"id": 1, "name": "Case_B", "operator": "bob"}]


@pytest.mark.unit
def test_controller_add_returns_public_row_dict(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(case_controller_module, "CaseModel", _FakeModel)

    controller = case_controller_module.Case()

    added = controller.add({"name": "Case_C", "operator": "carol"})

    assert added == {"id": 2, "name": "Case_C", "operator": "carol"}
    assert sorted(controller.names) == ["Case_A", "Case_C"]
