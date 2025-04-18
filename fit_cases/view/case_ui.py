#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6 import QtCore, QtGui, QtWidgets

from fit_cases.lang import load_translations
from fit_common.core.utils import get_version


class Ui_case_dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 600)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        Dialog.setMaximumSize(QtCore.QSize(800, 600))
        self.styleSheet = QtWidgets.QFrame(parent=Dialog)
        self.styleSheet.setGeometry(QtCore.QRect(-1, -1, 800, 600))
        self.styleSheet.setMaximumSize(QtCore.QSize(800, 600))
        self.styleSheet.setStyleSheet(
            "\n"
            "\n"
            "QWidget{\n"
            "    color: rgb(221, 221, 221);\n"
            "    font: 13px;\n"
            "}\n"
            "\n"
            "/* Tooltip */\n"
            "QToolTip {\n"
            "    color: #e06133;\n"
            "    background-color: rgba(33, 37, 43, 180);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "    background-image: none;\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 2px solid rgb(224, 97, 51);\n"
            "    text-align: left;\n"
            "    padding-left: 8px;\n"
            "    margin: 0px;\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#title_right_info { font: 13px; }\n"
            "#title_right_info { padding-left: 10px; }\n"
            "\n"
            "/* Content App */\n"
            "#content_top_bg{    \n"
            "    background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#content_bottom{\n"
            "    border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#right_buttons_container .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#right_buttons_container .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#right_buttons_container .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottom_bar { background-color: rgb(44, 49, 58); }\n"
            "#bottom_bar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "\n"
            "/* LineEdit */\n"
            "QLineEdit {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-left: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "QLineEdit::disabled {\n"
            "    color: rgba(255, 255, 255, 10%);\n"
            "}\n"
            "\n"
            "QLabel::disabled {\n"
            "    color: rgba(255, 255, 255, 10%);\n"
            "}\n"
            "\n"
            "/* PlainTextEdit */\n"
            "QPlainTextEdit {\n"
            "    background-color: rgb(27, 29, 35);\n"
            "    border-radius: 5px;\n"
            "    padding: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QPlainTextEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "    border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "    border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    subcontrol-position: left;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
            "{\n"
            "     background: none;\n"
            "}\n"
            " QScrollBar:vertical {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "    border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {    \n"
            "    background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "    border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "    border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "    border-top-left-radius: 4px;\n"
            "    border-top-right-radius: 4px;\n"
            "     subcontrol-position: top;\n"
            "     subcontrol-origin: margin;\n"
            " }\n"
            " QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            " QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
            "     background: none;\n"
            " }\n"
            "\n"
            "/* ComboBox */\n"
            "QComboBox{\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-bottom: 5px;\n"
            "    padding-top: 5px;\n"
            "    padding-left: 10px;\n"
            "\n"
            "}\n"
            "QComboBox:hover{\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 25px; \n"
            "    border-left-width: 3px;\n"
            "    border-left-color: rgba(39, 44, 54, 150);\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "\n"
            "QComboBox:!editable{\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    border: none;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "    padding:10px;\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            ""
        )
        self.styleSheet.setObjectName("styleSheet")
        self.styleSheetLayout = QtWidgets.QVBoxLayout(self.styleSheet)
        self.styleSheetLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMaximumSize
        )
        self.styleSheetLayout.setContentsMargins(10, 10, 10, 10)
        self.styleSheetLayout.setObjectName("styleSheetLayout")
        self.bg_app = QtWidgets.QFrame(parent=self.styleSheet)
        self.bg_app.setStyleSheet("background-color: rgb(44, 49, 58);")
        self.bg_app.setObjectName("bg_app")
        self.bgAppLayout = QtWidgets.QVBoxLayout(self.bg_app)
        self.bgAppLayout.setContentsMargins(0, -1, 0, 0)
        self.bgAppLayout.setObjectName("bgAppLayout")
        self.content_box = QtWidgets.QFrame(parent=self.bg_app)
        self.content_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_box.setObjectName("content_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content_box)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content_top_bg = QtWidgets.QFrame(parent=self.content_box)
        self.content_top_bg.setMinimumSize(QtCore.QSize(0, 50))
        self.content_top_bg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.content_top_bg.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_top_bg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_top_bg.setObjectName("content_top_bg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_top_bg)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_box = QtWidgets.QFrame(parent=self.content_top_bg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_box.sizePolicy().hasHeightForWidth())
        self.left_box.setSizePolicy(sizePolicy)
        self.left_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_box.setObjectName("left_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.left_box)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_container_2 = QtWidgets.QFrame(parent=self.left_box)
        self.logo_container_2.setMinimumSize(QtCore.QSize(60, 0))
        self.logo_container_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.logo_container_2.setObjectName("logo_container_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.logo_container_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.top_logo = QtWidgets.QLabel(parent=self.logo_container_2)
        self.top_logo.setMinimumSize(QtCore.QSize(42, 42))
        self.top_logo.setMaximumSize(QtCore.QSize(42, 42))
        self.top_logo.setText("")
        self.top_logo.setPixmap(QtGui.QPixmap(":/images/images/logo-42x42.png"))
        self.top_logo.setObjectName("top_logo")
        self.horizontalLayout_8.addWidget(self.top_logo)
        self.horizontalLayout_3.addWidget(self.logo_container_2)
        self.title_right_info = QtWidgets.QLabel(parent=self.left_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title_right_info.sizePolicy().hasHeightForWidth()
        )
        self.title_right_info.setSizePolicy(sizePolicy)
        self.title_right_info.setMaximumSize(QtCore.QSize(16777215, 45))
        self.title_right_info.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.title_right_info.setObjectName("title_right_info")
        self.horizontalLayout_3.addWidget(self.title_right_info)
        self.horizontalLayout.addWidget(self.left_box)
        self.right_buttons_container = QtWidgets.QFrame(parent=self.content_top_bg)
        self.right_buttons_container.setMinimumSize(QtCore.QSize(0, 28))
        self.right_buttons_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.right_buttons_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_buttons_container.setObjectName("right_buttons_container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.right_buttons_container)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.minimize_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.minimize_button.setMinimumSize(QtCore.QSize(28, 28))
        self.minimize_button.setMaximumSize(QtCore.QSize(28, 28))
        self.minimize_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.minimize_button.setToolTip("")
        self.minimize_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_minimize-disabled.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QtCore.QSize(20, 20))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_2.addWidget(self.minimize_button)
        self.close_button = QtWidgets.QPushButton(parent=self.right_buttons_container)
        self.close_button.setMinimumSize(QtCore.QSize(28, 28))
        self.close_button.setMaximumSize(QtCore.QSize(28, 28))
        self.close_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.close_button.setToolTip("")
        self.close_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_close-disabled.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QtCore.QSize(20, 20))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.horizontalLayout.addWidget(
            self.right_buttons_container, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout_2.addWidget(self.content_top_bg)
        self.content_bottom = QtWidgets.QFrame(parent=self.content_box)
        self.content_bottom.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_bottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_bottom.setObjectName("content_bottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.content_bottom)
        self.verticalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content = QtWidgets.QFrame(parent=self.content_bottom)
        self.content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content.setStyleSheet("background-color: rgb(40, 44, 52);\n" "")
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.case_info = QtWidgets.QFrame(parent=self.content)
        self.case_info.setMaximumSize(QtCore.QSize(16777215, 409))
        self.case_info.setObjectName("case_info")
        self.caseInfo = QtWidgets.QHBoxLayout(self.case_info)
        self.caseInfo.setContentsMargins(1, 1, 1, 1)
        self.caseInfo.setObjectName("caseInfo")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.caseInfo.addItem(spacerItem)
        self.form = QtWidgets.QFrame(parent=self.case_info)
        self.form.setMinimumSize(QtCore.QSize(460, 0))
        self.form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.form.setObjectName("form")
        self.form_layout = QtWidgets.QVBoxLayout(self.form)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(8)
        self.form_layout.setObjectName("form_layout")
        self.temporary_msg = QtWidgets.QLabel(parent=self.form)
        self.temporary_msg.setWordWrap(True)
        self.temporary_msg.setObjectName("temporary_msg")
        self.form_layout.addWidget(self.temporary_msg)
        self.name = QtWidgets.QComboBox(parent=self.form)
        self.name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.name.setAutoFillBackground(False)
        self.name.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.name.setEditable(True)
        self.name.setIconSize(QtCore.QSize(16, 16))
        self.name.setFrame(True)
        self.name.setObjectName("name")
        self.form_layout.addWidget(self.name)
        self.temporary_name = QtWidgets.QLineEdit(parent=self.form)
        self.temporary_name.setMinimumSize(QtCore.QSize(0, 30))
        self.temporary_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.temporary_name.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.temporary_name.setText("")
        self.temporary_name.setObjectName("temporary_name")
        self.form_layout.addWidget(self.temporary_name)
        self.lawyer_name = QtWidgets.QLineEdit(parent=self.form)
        self.lawyer_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lawyer_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lawyer_name.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.lawyer_name.setText("")
        self.lawyer_name.setObjectName("lawyer_name")
        self.form_layout.addWidget(self.lawyer_name)
        self.operator = QtWidgets.QLineEdit(parent=self.form)
        self.operator.setMinimumSize(QtCore.QSize(0, 30))
        self.operator.setMaximumSize(QtCore.QSize(300, 16777215))
        self.operator.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.operator.setText("")
        self.operator.setObjectName("operator")
        self.form_layout.addWidget(self.operator)
        self.proceeding_type = QtWidgets.QComboBox(parent=self.form)
        self.proceeding_type.setMaximumSize(QtCore.QSize(300, 16777215))
        self.proceeding_type.setMouseTracking(True)
        self.proceeding_type.setAutoFillBackground(False)
        self.proceeding_type.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.proceeding_type.setEditable(True)
        self.proceeding_type.setCurrentText("")
        self.proceeding_type.setIconSize(QtCore.QSize(16, 16))
        self.proceeding_type.setFrame(True)
        self.proceeding_type.setObjectName("proceeding_type")
        self.form_layout.addWidget(self.proceeding_type)
        self.courthouse = QtWidgets.QLineEdit(parent=self.form)
        self.courthouse.setMinimumSize(QtCore.QSize(0, 30))
        self.courthouse.setMaximumSize(QtCore.QSize(300, 16777215))
        self.courthouse.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.courthouse.setText("")
        self.courthouse.setObjectName("courthouse")
        self.form_layout.addWidget(self.courthouse)
        self.proceeding_number = QtWidgets.QLineEdit(parent=self.form)
        self.proceeding_number.setMinimumSize(QtCore.QSize(0, 30))
        self.proceeding_number.setMaximumSize(QtCore.QSize(300, 16777215))
        self.proceeding_number.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.proceeding_number.setText("")
        self.proceeding_number.setObjectName("proceeding_number")
        self.form_layout.addWidget(self.proceeding_number)
        self.logo_container = QtWidgets.QFrame(parent=self.form)
        self.logo_container.setMinimumSize(QtCore.QSize(0, 0))
        self.logo_container.setMaximumSize(QtCore.QSize(16777215, 40))
        self.logo_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.logo_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.logo_container.setObjectName("logo_container")
        self.logo_layout = QtWidgets.QHBoxLayout(self.logo_container)
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_layout.setObjectName("logo_layout")
        self.logo = QtWidgets.QLineEdit(parent=self.logo_container)
        self.logo.setMinimumSize(QtCore.QSize(300, 30))
        self.logo.setMaximumSize(QtCore.QSize(300, 16777215))
        self.logo.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.logo_layout.addWidget(self.logo)
        self.label = QtWidgets.QLabel(parent=self.logo_container)
        self.label.setMaximumSize(QtCore.QSize(16, 16))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/info-circle-disabled.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.logo_layout.addWidget(self.label)
        self.logo_button = QtWidgets.QPushButton(parent=self.logo_container)
        self.logo_button.setMinimumSize(QtCore.QSize(0, 30))
        self.logo_button.setMaximumSize(QtCore.QSize(1677721, 16777215))
        self.logo_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/cil-folder-open.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.logo_button.setIcon(icon2)
        self.logo_button.setObjectName("logo_button")
        self.logo_layout.addWidget(self.logo_button)
        self.form_layout.addWidget(self.logo_container)
        self.notes = QtWidgets.QPlainTextEdit(parent=self.form)
        self.notes.setMinimumSize(QtCore.QSize(0, 0))
        self.notes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notes.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.notes.setObjectName("notes")
        self.form_layout.addWidget(self.notes)
        self.caseInfo.addWidget(self.form)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.caseInfo.addItem(spacerItem1)
        self.horizontalLayout_4.addWidget(self.case_info)
        self.verticalLayout_6.addWidget(self.content)
        self.buttons = QtWidgets.QFrame(parent=self.content_bottom)
        self.buttons.setMaximumSize(QtCore.QSize(16777215, 40))
        self.buttons.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.buttons.setObjectName("buttons")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.buttons)
        self.horizontalLayout_6.setContentsMargins(20, 0, 20, 20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem2)
        self.save_button = QtWidgets.QPushButton(parent=self.buttons)
        self.save_button.setEnabled(True)
        self.save_button.setMinimumSize(QtCore.QSize(80, 30))
        self.save_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.save_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.save_button.setStyleSheet(
            "QPushButton:disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_6.addWidget(self.save_button)
        spacerItem3 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem3)
        self.cancel_button = QtWidgets.QPushButton(parent=self.buttons)
        self.cancel_button.setEnabled(True)
        self.cancel_button.setMinimumSize(QtCore.QSize(80, 30))
        self.cancel_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.cancel_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.cancel_button.setStyleSheet(
            ":disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_6.addWidget(self.cancel_button)
        self.verticalLayout_6.addWidget(self.buttons)
        self.bottom_bar = QtWidgets.QFrame(parent=self.content_bottom)
        self.bottom_bar.setMinimumSize(QtCore.QSize(0, 22))
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.credits_label = QtWidgets.QLabel(parent=self.bottom_bar)
        self.credits_label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.credits_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.credits_label.setObjectName("credits_label")
        self.horizontalLayout_5.addWidget(self.credits_label)
        self.version = QtWidgets.QLabel(parent=self.bottom_bar)
        self.version.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.version.setObjectName("version")
        self.horizontalLayout_5.addWidget(self.version)
        self.frame_size_grip = QtWidgets.QFrame(parent=self.bottom_bar)
        self.frame_size_grip.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_5.addWidget(self.frame_size_grip)
        self.verticalLayout_6.addWidget(self.bottom_bar)
        self.verticalLayout_2.addWidget(self.content_bottom)
        self.bgAppLayout.addWidget(self.content_box)
        self.styleSheetLayout.addWidget(self.bg_app)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle("FIT Case")

        self.translations = load_translations()

        self.title_right_info.setText(self.translations["TITLE"])
        self.temporary_msg.setText(self.translations["TEMPORARY_MSG"])
        self.temporary_name.setPlaceholderText(self.translations["TEMPORARY_NAME"])
        self.lawyer_name.setPlaceholderText(self.translations["LAWYER"])
        self.operator.setPlaceholderText(self.translations["OPERATOR"])
        self.courthouse.setPlaceholderText(self.translations["COURTHOUSE"])
        self.proceeding_number.setPlaceholderText(
            self.translations["PROCEEDING_NUMBER"]
        )
        self.logo.setPlaceholderText(self.translations["LOGO"])
        self.logo_button.setText(self.translations["LOGO_BUTTON"])
        self.notes.setPlaceholderText(self.translations["NOTES"])
        self.save_button.setText(self.translations["SAVE_BUTTON"])
        self.cancel_button.setText(self.translations["CANCEL_BUTTON"])
        self.credits_label.setText("By: fit-project.org")
        self.version.setText(get_version())
