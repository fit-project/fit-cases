from __future__ import annotations

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
        self.controller = SimpleNamespace(names=[])
        self.cases = []

    def set_case_information(self):
        return None

    def get_current_case_info(self):
        return {"name": "X"}


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


@pytest.mark.e2e
def test_new_dialog_enables_save_when_name_is_typed(
    qapp: QtWidgets.QApplication,
    patch_dialog_dependencies,
) -> None:
    dialog = dialog_module.CaseFormDialog()

    assert dialog.ui.save_button.isEnabled() is False

    dialog.ui.name.lineEdit().setText("Case A")
    qapp.processEvents()

    assert dialog.ui.save_button.isEnabled() is True
    assert "New" in dialog.ui.title_right_info.text()


@pytest.mark.e2e
def test_temporary_dialog_enables_save_when_temporary_name_is_typed(
    qapp: QtWidgets.QApplication,
    patch_dialog_dependencies,
) -> None:
    dialog = dialog_module.CaseFormDialog(temporary=True)

    assert dialog.ui.save_button.isEnabled() is False

    dialog.ui.temporary_name.setText("Temporary Case")
    qapp.processEvents()

    assert dialog.ui.save_button.isEnabled() is True
    assert "Temporary" in dialog.ui.title_right_info.text()
