#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6 import QtCore, QtWidgets

from fit_cases.view.case_form_manager import CaseFormManager
from fit_common.core.utility import get_version

from fit_cases.controller.case import Case as CaseController
from fit_cases.lang import load_translations


from fit_cases.view.case_ui import (
    Ui_case_dialog,
)

from fit_assets import resources


class CaseFormDialog(QtWidgets.QDialog):
    def __init__(self, case_info=None, temporary=False, parent=None):
        super().__init__(parent)
        self.__temporary = temporary
        self.__case_info = case_info

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

        # TEMPORARY CASE NAME
        case_name = self.translations["TEMPORARY_CASE_NAME"]
        id = -1
        if self.__temporary is True:
            self.ui.name.hide()
            self.ui.save_button.setEnabled(False)
            self.ui.temporary_name.textChanged.connect(self.__enable_save_button)
        else:
            self.ui.temporary_name.hide()
            self.ui.temporary_msg.hide()
            if self.__case_info is not None:
                case_name = self.__case_info.get("name")
                self.ui.name.setCurrentText(case_name)
            self.ui.name.lineEdit().setReadOnly(True)

            if (
                case_name not in self.form_manager.controller.names
                and self.__case_info is not None
            ):
                self.form_manager.cases.append(self.__case_info)
            if self.__case_info is not None:
                if "id" in self.__case_info:
                    id = self.__case_info.get("id")

        self.ui.title_right_info.setText(
            self.translations["DIALOG_TITLE"].format(case_name, str(id))
        )
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

    def get_case_info(self):
        return self.__case_info

    def accept(self):
        self.__case_info = self.form_manager.get_current_case_info()
        if self.__temporary is False:
            CaseController().cases = self.__case_info
        return super().accept()

    def reject(self):
        return super().reject()
