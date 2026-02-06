#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

import base64
import json
import os
from enum import Enum

from fit_common.core import get_version
from fit_common.gui.dialog import Dialog, DialogButtonTypes
from fit_common.gui.ui_translation import translate_ui
from PySide6 import QtCore, QtWidgets

from fit_cases.controller.case import Case as CaseController
from fit_cases.lang import load_translations
from fit_cases.view.case_form_manager import CaseFormManager
from fit_cases.view.case_ui import (
    Ui_case_dialog,
)


class CaseMode(Enum):
    EXISTING = "existing"
    TEMPORARY = "temporary"
    NEW = "new"


from fit_assets import resources  # noqa: F401


class CaseFormDialog(QtWidgets.QDialog):
    def __init__(self, case_info=None, temporary=False, parent=None):
        super().__init__(parent)
        self.__temporary = temporary
        self.__case_info = case_info

        if case_info is not None:
            self.__mode = CaseMode.EXISTING
        elif temporary:
            self.__mode = CaseMode.TEMPORARY
        else:
            self.__mode = CaseMode.NEW

        self.translations = load_translations()

        self.__init_ui()

    def __init_ui(self):

        # HIDE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui = Ui_case_dialog()
        self.ui.setupUi(self)

        # CUSTOM TOP BAR
        self.ui.left_box.mouseMoveEvent = self.move_window

        # MINIMIZE BUTTON
        self.ui.minimize_button.clicked.connect(self.showMinimized)

        # CLOSE BUTTON
        self.ui.close_button.clicked.connect(self.close)

        # SET VERSION
        self.ui.version.setText(get_version())

        # CANCEL BUTTON
        self.ui.cancel_button.clicked.connect(self.reject)

        # SAVE BUTTON
        self.ui.save_button.clicked.connect(self.accept)

        # FORM MANAGER
        self.form_manager = CaseFormManager(self.ui.form, self.__temporary)
        self.form_manager.case_found.connect(self.__on_case_found)
        self.form_manager.case_not_found.connect(self.__on_case_not_found)

        case_name = ""
        case_id = -1

        translate_ui(self.translations, self)

        if self.__mode == CaseMode.TEMPORARY:
            # TEMPORARY CASE NAME
            case_name = self.translations["TEMPORARY_CASE_NAME"]
            case_id = -1
            self.ui.name.hide()
            self.ui.save_button.setEnabled(False)
            self.ui.temporary_name.textChanged.connect(self.__enable_save_button)
        elif self.__mode == CaseMode.EXISTING:
            self.ui.temporary_name.hide()
            self.ui.temporary_msg.hide()
            if self.__case_info is not None:
                case_name = self.__case_info.get("name", "")
                self.ui.name.setCurrentText(case_name)
                case_id = self.__case_info.get("id", -1)
            else:
                self.ui.save_button.setEnabled(False)

            self.ui.name.lineEdit().setReadOnly(True)

            if (
                case_name not in self.form_manager.controller.names
                and self.__case_info is not None
            ):
                self.form_manager.cases.append(self.__case_info)
            if self.__case_info is not None:
                if "id" in self.__case_info:
                    id = self.__case_info.get("id")
        elif self.__mode == CaseMode.NEW:
            case_name = self.translations["NEW_CASE_NAME"]
            case_id = -1
            self.ui.temporary_name.hide()
            self.ui.temporary_msg.hide()
            self.ui.name.setEditable(True)
            self.ui.name.lineEdit().setReadOnly(False)
            self.ui.name.setCurrentText("")
            self.ui.save_button.setEnabled(False)
            self.ui.name.lineEdit().textChanged.connect(self.__enable_save_button)

        self.ui.title_right_info.setText(
            self.translations["DIALOG_TITLE"].format(case_name, str(case_id))
        )

        self.ui.save_button.setDefault(True)

        self.form_manager.set_case_information()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def move_window(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def __enable_save_button(self, text):
        self.ui.save_button.setEnabled(bool(text))

    def __on_case_found(self, case_info):
        if self.__mode == CaseMode.NEW:
            self.__mode = CaseMode.EXISTING
            self.ui.title_right_info.setText(
                self.translations["DIALOG_TITLE"].format(
                    case_info.get("name"), str(case_info.get("id"))
                )
            )

    def __on_case_not_found(self):
        if self.__mode == CaseMode.EXISTING:
            self.__mode = CaseMode.NEW
            self.ui.title_right_info.setText(
                self.translations["DIALOG_TITLE"].format(
                    self.translations["NEW_CASE_NAME"], str(-1)
                )
            )

    def get_case_info(self, acquisition_directory=None):
        if acquisition_directory is None:
            return self.__case_info
        else:
            file = os.path.join(acquisition_directory, "caseinfo.json")

            case_info = {}

            if os.path.isfile(file):
                with open(file, "r") as f:
                    case_info = json.load(f)
                    logo_bin = case_info.get("logo_bin")
                if logo_bin:
                    case_info["logo_bin"] = base64.b64decode(bytes(logo_bin, "utf-8"))
            else:
                dialog = Dialog(
                    self.translations["TITLE"],
                    self.translations["WAR_NOT_CASE_INFO_JSON_FILE_FOUND"],
                )
                dialog.message.setStyleSheet("font-size: 13px;")
                dialog.set_buttons_type(DialogButtonTypes.QUESTION)
                dialog.right_button.clicked.connect(
                    lambda: self.__get_temporary_case_info(dialog, case_info, False)
                )
                dialog.left_button.clicked.connect(
                    lambda: self.__get_temporary_case_info(dialog, case_info, True)
                )

                dialog.exec()

            return case_info

    def __get_temporary_case_info(self, dialog, case_info, temporary=False):
        dialog.close()
        __case_info = {
            "name": "Unknown",
            "operator": "",
            "courthouse": "",
            "notes": "",
            "logo": "",
            "logo_width": "",
            "lawyer_name": "",
            "proceeding_type": 0,
            "proceeding_number": "",
            "logo_bin": None,
            "logo_height": "",
        }

        if temporary:
            case_form = CaseFormDialog(temporary=True)
            return_value = case_form.exec()
            if return_value:
                __case_info = case_form.get_case_info()
                if os.path.isfile(__case_info.get("logo")):
                    __case_info["logo_bin"] = self.__set_logo_bin(
                        __case_info.get("logo")
                    )
                else:
                    __case_info["logo_bin"] = None

        case_info.update(__case_info)

    def __set_logo_bin(self, file_path):
        with open(file_path, "rb") as file:
            return file.read()

    def accept(self):
        self.__case_info = self.form_manager.get_current_case_info()
        if self.__mode in [CaseMode.EXISTING]:
            CaseController().cases = self.__case_info
        elif self.__mode in [CaseMode.NEW]:
            CaseController().add(self.__case_info)
        return super().accept()

    def reject(self):
        return super().reject()
