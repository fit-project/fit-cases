from __future__ import annotations

import base64
import json
from pathlib import Path
from types import SimpleNamespace

import pytest
from PySide6 import QtCore, QtWidgets

from fit_cases.view import case_form_dialog as dialog_module


class FakeUiCaseDialog:
    def setupUi(self, dialog: QtWidgets.QDialog) -> None:
        self.left_box = QtWidgets.QWidget(dialog)
        self.minimize_button = QtWidgets.QPushButton(dialog)
        self.close_button = QtWidgets.QPushButton(dialog)
        self.version = QtWidgets.QLabel(dialog)
        self.cancel_button = QtWidgets.QPushButton(dialog)
        self.save_button = QtWidgets.QPushButton(dialog)
        self.form = QtWidgets.QWidget(dialog)
        self.title_right_info = QtWidgets.QLabel(dialog)

        self.name = QtWidgets.QComboBox(dialog)
        self.name.setEditable(True)

        self.temporary_name = QtWidgets.QLineEdit(dialog)
        self.temporary_msg = QtWidgets.QLabel(dialog)


class FakeCaseFormManager(QtCore.QObject):
    case_found = QtCore.Signal(dict)
    case_not_found = QtCore.Signal()

    def __init__(self, form, temporary=False, parent=None):
        super().__init__(parent)
        self.controller = SimpleNamespace(names=["Existing"])
        self.cases = []
        self._case_info = {
            "id": 99,
            "name": "CaseFromForm",
            "operator": "op",
        }

    def set_case_information(self):
        return None

    def get_current_case_info(self):
        return self._case_info


@pytest.fixture
def patch_dialog_dependencies(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(dialog_module, "Ui_case_dialog", FakeUiCaseDialog)
    monkeypatch.setattr(dialog_module, "CaseFormManager", FakeCaseFormManager)
    monkeypatch.setattr(dialog_module, "translate_ui", lambda *_: None)
    monkeypatch.setattr(dialog_module, "get_version", lambda: "1.2.3")
    monkeypatch.setattr(
        dialog_module,
        "load_translations",
        lambda: {
            "DIALOG_TITLE": " Case {} ID: {}",
            "TEMPORARY_CASE_NAME": "Temporary",
            "NEW_CASE_NAME": "New",
            "TITLE": "Case Info",
            "WAR_NOT_CASE_INFO_JSON_FILE_FOUND": "missing",
        },
    )


@pytest.mark.integration
def test_get_case_info_reads_caseinfo_json_and_decodes_logo(
    qapp: QtWidgets.QApplication,
    tmp_path: Path,
    patch_dialog_dependencies,
) -> None:
    logo_bytes = b"logo-binary"
    caseinfo_path = tmp_path / "caseinfo.json"
    caseinfo_path.write_text(
        json.dumps(
            {
                "name": "A",
                "logo_bin": base64.b64encode(logo_bytes).decode("utf-8"),
            }
        ),
        encoding="utf-8",
    )

    dialog = dialog_module.CaseFormDialog()

    loaded = dialog.get_case_info(str(tmp_path))

    assert loaded["name"] == "A"
    assert loaded["logo_bin"] == logo_bytes


@pytest.mark.integration
def test_accept_existing_mode_updates_case(
    qapp: QtWidgets.QApplication,
    patch_dialog_dependencies,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = {"updated": None, "added": None}

    class FakeController:
        @property
        def cases(self):
            return []

        @cases.setter
        def cases(self, value):
            calls["updated"] = value

        def add(self, value):
            calls["added"] = value

    monkeypatch.setattr(dialog_module, "CaseController", FakeController)

    dialog = dialog_module.CaseFormDialog(case_info={"id": 1, "name": "Existing"})
    dialog.accept()

    assert calls["updated"] == {"id": 99, "name": "CaseFromForm", "operator": "op"}
    assert calls["added"] is None


@pytest.mark.integration
def test_accept_new_mode_adds_case(
    qapp: QtWidgets.QApplication,
    patch_dialog_dependencies,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls = {"updated": None, "added": None}

    class FakeController:
        @property
        def cases(self):
            return []

        @cases.setter
        def cases(self, value):
            calls["updated"] = value

        def add(self, value):
            calls["added"] = value

    monkeypatch.setattr(dialog_module, "CaseController", FakeController)

    dialog = dialog_module.CaseFormDialog()
    dialog.accept()

    assert calls["updated"] is None
    assert calls["added"] == {"id": 99, "name": "CaseFromForm", "operator": "op"}
