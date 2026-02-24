from __future__ import annotations

from types import SimpleNamespace

import pytest
from PySide6 import QtWidgets

from fit_cases.view import case_form_manager as manager_module


def _translations() -> dict[str, str]:
    return {
        "LOGO_INFO": "Minimum width: {}px, Format: {}, Background: {}",
        "SELECT_EMPTY_LOGO": "Browse...",
        "SELECT_FULL_LOGO": "Change...",
        "SELECT_PROCEEDING_TYPE": "Select proceeding type...",
        "SELECT_CASE_NAME": "Select case...",
        "CHECK_SELECTED_LOGO": "Check logo file",
        "ERR_SELECTED_LOGO_FORMAT": "fmt",
        "ERR_SELECTED_LOGO_MINIMUM_WIDTH": "min",
        "ERR_SELECTED_LOGO_BG_COLOR": "bg",
    }


def _build_form() -> QtWidgets.QWidget:
    form = QtWidgets.QWidget()

    name = QtWidgets.QComboBox(form)
    name.setObjectName("name")
    name.setEditable(True)

    proceeding_type = QtWidgets.QComboBox(form)
    proceeding_type.setObjectName("proceeding_type")
    proceeding_type.setEditable(True)

    field_names = [
        "id",
        "lawyer_name",
        "operator",
        "courthouse",
        "proceeding_number",
    ]
    for field_name in field_names:
        field = QtWidgets.QLineEdit(form)
        field.setObjectName(field_name)

    notes = QtWidgets.QPlainTextEdit(form)
    notes.setObjectName("notes")

    logo_container = QtWidgets.QFrame(form)
    logo_container.setObjectName("logo_container")

    logo_layout = QtWidgets.QHBoxLayout(logo_container)

    logo_path = QtWidgets.QLineEdit(logo_container)
    logo_path.setObjectName("logo")
    logo_layout.addWidget(logo_path)

    logo_button = QtWidgets.QPushButton(logo_container)
    logo_layout.addWidget(logo_button)

    QtWidgets.QLabel(logo_container)

    return form


class _FakeCaseController:
    def __init__(self):
        self.cases = [
            {
                "id": 1,
                "name": "Case_A",
                "lawyer_name": "Lawyer",
                "operator": "Operator",
                "proceeding_type": 2,
                "courthouse": "Milan",
                "proceeding_number": 123,
                "notes": "note",
                "logo": "",
                "logo_bin": None,
            }
        ]
        self.keys = [
            "id",
            "name",
            "lawyer_name",
            "operator",
            "proceeding_type",
            "courthouse",
            "proceeding_number",
            "notes",
            "logo",
            "logo_bin",
        ]


@pytest.mark.integration
def test_set_case_information_found_populates_form_and_emits_signal(
    qapp: QtWidgets.QApplication,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(manager_module, "CaseController", _FakeCaseController)
    monkeypatch.setattr(
        manager_module,
        "LegalProceedingTypeController",
        lambda: SimpleNamespace(proceedings=[{"id": 2, "name": "Penale"}]),
    )
    monkeypatch.setattr(manager_module, "load_translations", _translations)

    form = _build_form()
    manager = manager_module.CaseFormManager(form)

    found_payloads: list[dict] = []
    manager.case_found.connect(lambda payload: found_payloads.append(payload))

    manager.name.setCurrentText("Case_A")
    manager.set_case_information()

    assert found_payloads and found_payloads[-1]["name"] == "Case_A"
    assert form.findChild(QtWidgets.QLineEdit, "lawyer_name").text() == "Lawyer"
    assert form.findChild(QtWidgets.QComboBox, "proceeding_type").currentData() == 2
    assert manager.logo_button.text() == "Browse..."


@pytest.mark.integration
def test_set_case_information_not_found_clears_form_and_emits_signal(
    qapp: QtWidgets.QApplication,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(manager_module, "CaseController", _FakeCaseController)
    monkeypatch.setattr(
        manager_module,
        "LegalProceedingTypeController",
        lambda: SimpleNamespace(proceedings=[{"id": 2, "name": "Penale"}]),
    )
    monkeypatch.setattr(manager_module, "load_translations", _translations)

    form = _build_form()
    manager = manager_module.CaseFormManager(form)

    form.findChild(QtWidgets.QLineEdit, "lawyer_name").setText("stale")
    form.findChild(QtWidgets.QPlainTextEdit, "notes").setPlainText("stale")

    not_found_calls = {"count": 0}
    manager.case_not_found.connect(
        lambda: not_found_calls.__setitem__("count", not_found_calls["count"] + 1)
    )

    manager.name.setCurrentText("unknown")
    manager.set_case_information()

    assert not_found_calls["count"] >= 1
    assert form.findChild(QtWidgets.QLineEdit, "lawyer_name").text() == ""
    assert form.findChild(QtWidgets.QPlainTextEdit, "notes").toPlainText() == ""
    assert form.findChild(QtWidgets.QComboBox, "proceeding_type").currentIndex() == -1


@pytest.mark.integration
def test_get_current_case_info_collects_and_maps_values(
    qapp: QtWidgets.QApplication,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(manager_module, "CaseController", _FakeCaseController)
    monkeypatch.setattr(
        manager_module,
        "LegalProceedingTypeController",
        lambda: SimpleNamespace(
            proceedings=[
                {"id": 2, "name": "Penale"},
                {"id": 3, "name": "Civile"},
            ]
        ),
    )
    monkeypatch.setattr(manager_module, "load_translations", _translations)

    form = _build_form()
    manager = manager_module.CaseFormManager(form)

    manager.name.setCurrentText("Case_New")
    form.findChild(QtWidgets.QLineEdit, "lawyer_name").setText("L")
    form.findChild(QtWidgets.QLineEdit, "operator").setText("O")
    form.findChild(QtWidgets.QLineEdit, "courthouse").setText("Rome")
    form.findChild(QtWidgets.QLineEdit, "proceeding_number").setText("99")
    form.findChild(QtWidgets.QLineEdit, "logo").setText("/tmp/logo.png")
    form.findChild(QtWidgets.QPlainTextEdit, "notes").setPlainText("N")
    form.findChild(QtWidgets.QComboBox, "proceeding_type").setCurrentText("Civile")
    manager.logo_height = "auto"
    manager.logo_width = "100"

    info = manager.get_current_case_info()

    assert info["name"] == "Case_New"
    assert info["proceeding_type"] == 3
    assert info["lawyer_name"] == "L"
    assert info["operator"] == "O"
    assert info["notes"] == "N"
    assert info["logo"] == "/tmp/logo.png"
    assert info["logo_bin"] is None
    assert info["logo_height"] == "auto"
    assert info["logo_width"] == "100"
