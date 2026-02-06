# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'case.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt
from PySide6.QtGui import QCursor, QIcon, QPixmap
from PySide6.QtWidgets import (
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
)


class Ui_case_dialog(object):
    def setupUi(self, case_dialog):
        if not case_dialog.objectName():
            case_dialog.setObjectName("case_dialog")
        case_dialog.resize(800, 600)
        case_dialog.setMinimumSize(QSize(800, 600))
        case_dialog.setMaximumSize(QSize(800, 600))
        self.styleSheet = QFrame(case_dialog)
        self.styleSheet.setObjectName("styleSheet")
        self.styleSheet.setGeometry(QRect(-1, -1, 800, 600))
        self.styleSheet.setMaximumSize(QSize(800, 600))
        self.styleSheet.setStyleSheet(
            "\n"
            "\n"
            "QWidget{\n"
            "	color: rgb(221, 221, 221);\n"
            "	font: 13px;\n"
            "}\n"
            "\n"
            "/* Tooltip */\n"
            "QToolTip {\n"
            "	color: #e06133;\n"
            "	background-color: rgba(33, 37, 43, 180);\n"
            "	border: 1px solid rgb(44, 49, 58);\n"
            "	background-image: none;\n"
            "	background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "	border: none;\n"
            "	border-left: 2px solid rgb(224, 97, 51);\n"
            "	text-align: left;\n"
            "	padding-left: 8px;\n"
            "	margin: 0px;\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#title_right_info { font: 13px; }\n"
            "#title_right_info { padding-left: 10px; }\n"
            "\n"
            "/* Content App */\n"
            "#content_top_bg{	\n"
            "	background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#content_bottom{\n"
            "	border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#right_buttons_container .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#right_buttons_container .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#right"
            "_buttons_container .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottom_bar { background-color: rgb(44, 49, 58); }\n"
            "#bottom_bar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "\n"
            "/* LineEdit */\n"
            "QLineEdit {\n"
            "	background-color: rgb(33, 37, 43);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "	padding-left: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
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
            "	background-color: rgb(27, 29, 35);\n"
            "	border-radius: 5px;\n"
            ""
            "	padding: 10px;\n"
            "	selection-color: rgb(255, 255, 255);\n"
            "	selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QPlainTextEdit:hover {\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "	border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* ScrollBars */\n"
            "QScrollBar:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    height: 8px;\n"
            "    margin: 0px 21px 0 21px;\n"
            "	border-radius: 0px;\n"
            "}\n"
            "QScrollBar::handle:horizontal {\n"
            "    background: rgb(189, 147, 249);\n"
            "    min-width: 25px;\n"
            "	border-radius: 4px\n"
            "}\n"
            "QScrollBar::add-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-right-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "    subcontrol-position: right;\n"
            "    subcontrol-origin: margin;\n"
            "}\n"
            "QScrollBar::sub"
            "-line:horizontal {\n"
            "    border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "    width: 20px;\n"
            "	border-top-left-radius: 4px;\n"
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
            "	border: none;\n"
            "    background: rgb(52, 59, 72);\n"
            "    width: 8px;\n"
            "    margin: 21px 0 21px 0;\n"
            "	border-radius: 0px;\n"
            " }\n"
            " QScrollBar::handle:vertical {	\n"
            "	background: rgb(189, 147, 249);\n"
            "    min-height: 25px;\n"
            "	border-radius: 4px\n"
            " }\n"
            " QScrollBar::add-line:vertical {\n"
            "     border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-bottom-left-radius: 4px;\n"
            "    border-bottom-right-radius: 4px;\n"
            "     subcontrol-position: bottom;\n"
            "     subcontrol-origin"
            ": margin;\n"
            " }\n"
            " QScrollBar::sub-line:vertical {\n"
            "	border: none;\n"
            "    background: rgb(55, 63, 77);\n"
            "     height: 20px;\n"
            "	border-top-left-radius: 4px;\n"
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
            "	background-color: rgb(33, 37, 43);\n"
            "	border-radius: 5px;\n"
            "	border: 2px solid rgb(33, 37, 43);\n"
            "    padding-bottom: 5px;\n"
            "    padding-top: 5px;\n"
            "    padding-left: 10px;\n"
            "\n"
            "}\n"
            "QComboBox:hover{\n"
            "	border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "	subcontrol-origin: padding;\n"
            "	subcontrol-position: top right;\n"
            "	width: 25px; \n"
            "	border-left-width: 3px;\n"
            "	border-left-color: rgba(39, 44, 54, 150);\n"
            "	border-left-style: solid;\n"
            ""
            "	border-top-right-radius: 3px;\n"
            "	border-bottom-right-radius: 3px;	\n"
            "	background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
            "	background-position: center;\n"
            "	background-repeat: no-reperat;\n"
            " }\n"
            "\n"
            "QComboBox:!editable{\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    border: none;\n"
            "	background-color: rgb(0, 0, 0);\n"
            "    padding:10px;\n"
            "	selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            ""
        )
        self.styleSheetLayout = QVBoxLayout(self.styleSheet)
        self.styleSheetLayout.setObjectName("styleSheetLayout")
        self.styleSheetLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.styleSheetLayout.setContentsMargins(10, 10, 10, 10)
        self.bg_app = QFrame(self.styleSheet)
        self.bg_app.setObjectName("bg_app")
        self.bg_app.setStyleSheet("background-color: rgb(44, 49, 58);")
        self.bgAppLayout = QVBoxLayout(self.bg_app)
        self.bgAppLayout.setObjectName("bgAppLayout")
        self.bgAppLayout.setContentsMargins(0, -1, 0, 0)
        self.content_box = QFrame(self.bg_app)
        self.content_box.setObjectName("content_box")
        self.content_box.setFrameShape(QFrame.NoFrame)
        self.content_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_box)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.content_top_bg = QFrame(self.content_box)
        self.content_top_bg.setObjectName("content_top_bg")
        self.content_top_bg.setMinimumSize(QSize(0, 50))
        self.content_top_bg.setMaximumSize(QSize(16777215, 50))
        self.content_top_bg.setFrameShape(QFrame.NoFrame)
        self.content_top_bg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.content_top_bg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.left_box = QFrame(self.content_top_bg)
        self.left_box.setObjectName("left_box")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_box.sizePolicy().hasHeightForWidth())
        self.left_box.setSizePolicy(sizePolicy)
        self.left_box.setFrameShape(QFrame.NoFrame)
        self.left_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.left_box)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.logo_container_2 = QFrame(self.left_box)
        self.logo_container_2.setObjectName("logo_container_2")
        self.logo_container_2.setMinimumSize(QSize(60, 0))
        self.logo_container_2.setMaximumSize(QSize(60, 16777215))
        self.horizontalLayout_8 = QHBoxLayout(self.logo_container_2)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.top_logo = QLabel(self.logo_container_2)
        self.top_logo.setObjectName("top_logo")
        self.top_logo.setMinimumSize(QSize(42, 42))
        self.top_logo.setMaximumSize(QSize(42, 42))
        self.top_logo.setPixmap(QPixmap(":/images/images/logo-42x42.png"))

        self.horizontalLayout_8.addWidget(self.top_logo)

        self.horizontalLayout_3.addWidget(self.logo_container_2)

        self.title_right_info = QLabel(self.left_box)
        self.title_right_info.setObjectName("title_right_info")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding
        )
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.title_right_info.sizePolicy().hasHeightForWidth()
        )
        self.title_right_info.setSizePolicy(sizePolicy1)
        self.title_right_info.setMaximumSize(QSize(16777215, 45))
        self.title_right_info.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.horizontalLayout_3.addWidget(self.title_right_info)

        self.horizontalLayout.addWidget(self.left_box)

        self.right_buttons_container = QFrame(self.content_top_bg)
        self.right_buttons_container.setObjectName("right_buttons_container")
        self.right_buttons_container.setMinimumSize(QSize(0, 28))
        self.right_buttons_container.setFrameShape(QFrame.NoFrame)
        self.right_buttons_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.right_buttons_container)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_button = QPushButton(self.right_buttons_container)
        self.minimize_button.setObjectName("minimize_button")
        self.minimize_button.setMinimumSize(QSize(28, 28))
        self.minimize_button.setMaximumSize(QSize(28, 28))
        self.minimize_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(
            ":/icons/icons/icon_minimize-disabled.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.minimize_button.setIcon(icon)
        self.minimize_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimize_button)

        self.close_button = QPushButton(self.right_buttons_container)
        self.close_button.setObjectName("close_button")
        self.close_button.setMinimumSize(QSize(28, 28))
        self.close_button.setMaximumSize(QSize(28, 28))
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(
            ":/icons/icons/icon_close-disabled.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.close_button.setIcon(icon1)
        self.close_button.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.close_button)

        self.horizontalLayout.addWidget(self.right_buttons_container, 0, Qt.AlignRight)

        self.verticalLayout_2.addWidget(self.content_top_bg)

        self.content_bottom = QFrame(self.content_box)
        self.content_bottom.setObjectName("content_bottom")
        self.content_bottom.setFrameShape(QFrame.NoFrame)
        self.content_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.content_bottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.content_bottom)
        self.content.setObjectName("content")
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.content.setStyleSheet("background-color: rgb(40, 44, 52);\n" "")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.case_info = QFrame(self.content)
        self.case_info.setObjectName("case_info")
        self.case_info.setMaximumSize(QSize(16777215, 409))
        self.caseInfo = QHBoxLayout(self.case_info)
        self.caseInfo.setObjectName("caseInfo")
        self.caseInfo.setContentsMargins(1, 1, 1, 1)
        self.leftSpacer1 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.caseInfo.addItem(self.leftSpacer1)

        self.form = QFrame(self.case_info)
        self.form.setObjectName("form")
        self.form.setMinimumSize(QSize(460, 0))
        self.form.setMaximumSize(QSize(16777215, 16777215))
        self.form_layout = QVBoxLayout(self.form)
        self.form_layout.setSpacing(8)
        self.form_layout.setObjectName("form_layout")
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.temporary_msg = QLabel(self.form)
        self.temporary_msg.setObjectName("temporary_msg")
        self.temporary_msg.setWordWrap(True)
        self.temporary_msg.setMargin(0)

        self.form_layout.addWidget(self.temporary_msg)

        self.name = QComboBox(self.form)
        self.name.setObjectName("name")
        self.name.setMaximumSize(QSize(300, 16777215))
        self.name.setAutoFillBackground(False)
        self.name.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.name.setEditable(True)
        self.name.setIconSize(QSize(16, 16))
        self.name.setFrame(True)

        self.form_layout.addWidget(self.name)

        self.temporary_name = QLineEdit(self.form)
        self.temporary_name.setObjectName("temporary_name")
        self.temporary_name.setMinimumSize(QSize(0, 30))
        self.temporary_name.setMaximumSize(QSize(300, 16777215))
        self.temporary_name.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.form_layout.addWidget(self.temporary_name)

        self.lawyer = QLineEdit(self.form)
        self.lawyer.setObjectName("lawyer")
        self.lawyer.setMinimumSize(QSize(0, 30))
        self.lawyer.setMaximumSize(QSize(300, 16777215))
        self.lawyer.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.form_layout.addWidget(self.lawyer)

        self.operator = QLineEdit(self.form)
        self.operator.setObjectName("operator")
        self.operator.setMinimumSize(QSize(0, 30))
        self.operator.setMaximumSize(QSize(300, 16777215))
        self.operator.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.form_layout.addWidget(self.operator)

        self.proceeding_type = QComboBox(self.form)
        self.proceeding_type.setObjectName("proceeding_type")
        self.proceeding_type.setMaximumSize(QSize(300, 16777215))
        self.proceeding_type.setMouseTracking(True)
        self.proceeding_type.setAutoFillBackground(False)
        self.proceeding_type.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.proceeding_type.setEditable(True)
        self.proceeding_type.setCurrentText("")
        self.proceeding_type.setIconSize(QSize(16, 16))
        self.proceeding_type.setFrame(True)

        self.form_layout.addWidget(self.proceeding_type)

        self.courthouse = QLineEdit(self.form)
        self.courthouse.setObjectName("courthouse")
        self.courthouse.setMinimumSize(QSize(0, 30))
        self.courthouse.setMaximumSize(QSize(300, 16777215))
        self.courthouse.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.form_layout.addWidget(self.courthouse)

        self.proceeding_number = QLineEdit(self.form)
        self.proceeding_number.setObjectName("proceeding_number")
        self.proceeding_number.setMinimumSize(QSize(0, 30))
        self.proceeding_number.setMaximumSize(QSize(300, 16777215))
        self.proceeding_number.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.form_layout.addWidget(self.proceeding_number)

        self.logo_container = QFrame(self.form)
        self.logo_container.setObjectName("logo_container")
        self.logo_container.setMinimumSize(QSize(0, 0))
        self.logo_container.setMaximumSize(QSize(16777215, 40))
        self.logo_container.setFrameShape(QFrame.NoFrame)
        self.logo_container.setFrameShadow(QFrame.Raised)
        self.logo_layout = QHBoxLayout(self.logo_container)
        self.logo_layout.setObjectName("logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLineEdit(self.logo_container)
        self.logo.setObjectName("logo")
        self.logo.setMinimumSize(QSize(300, 30))
        self.logo.setMaximumSize(QSize(300, 16777215))
        self.logo.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.logo_layout.addWidget(self.logo)

        self.label = QLabel(self.logo_container)
        self.label.setObjectName("label")
        self.label.setMaximumSize(QSize(16, 16))
        self.label.setPixmap(QPixmap(":/icons/icons/info-circle-disabled.png"))
        self.label.setScaledContents(True)

        self.logo_layout.addWidget(self.label)

        self.logo_button = QPushButton(self.logo_container)
        self.logo_button.setObjectName("logo_button")
        self.logo_button.setMinimumSize(QSize(0, 30))
        self.logo_button.setMaximumSize(QSize(1677721, 16777215))
        self.logo_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(
            ":/icons/icons/cil-folder-open.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off,
        )
        self.logo_button.setIcon(icon2)

        self.logo_layout.addWidget(self.logo_button)

        self.form_layout.addWidget(self.logo_container)

        self.notes = QPlainTextEdit(self.form)
        self.notes.setObjectName("notes")
        self.notes.setMinimumSize(QSize(0, 0))
        self.notes.setMaximumSize(QSize(16777215, 16777215))
        self.notes.setStyleSheet("background-color: rgb(33, 37, 43);")

        self.form_layout.addWidget(self.notes)

        self.caseInfo.addWidget(self.form)

        self.rigthSpacer1 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.caseInfo.addItem(self.rigthSpacer1)

        self.horizontalLayout_4.addWidget(self.case_info)

        self.verticalLayout_6.addWidget(self.content)

        self.buttons = QFrame(self.content_bottom)
        self.buttons.setObjectName("buttons")
        self.buttons.setMaximumSize(QSize(16777215, 40))
        self.buttons.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.horizontalLayout_6 = QHBoxLayout(self.buttons)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, 0, 20, 20)
        self.left_spacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.left_spacer)

        self.save_button = QPushButton(self.buttons)
        self.save_button.setObjectName("save_button")
        self.save_button.setEnabled(True)
        self.save_button.setMinimumSize(QSize(80, 30))
        self.save_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.save_button.setLayoutDirection(Qt.LeftToRight)
        self.save_button.setStyleSheet(
            "QPushButton:disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )

        self.horizontalLayout_6.addWidget(self.save_button)

        self.between_spacer = QSpacerItem(
            5, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_6.addItem(self.between_spacer)

        self.cancel_button = QPushButton(self.buttons)
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setEnabled(True)
        self.cancel_button.setMinimumSize(QSize(80, 30))
        self.cancel_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cancel_button.setLayoutDirection(Qt.LeftToRight)
        self.cancel_button.setStyleSheet(
            ":disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )

        self.horizontalLayout_6.addWidget(self.cancel_button)

        self.verticalLayout_6.addWidget(self.buttons)

        self.bottom_bar = QFrame(self.content_bottom)
        self.bottom_bar.setObjectName("bottom_bar")
        self.bottom_bar.setMinimumSize(QSize(0, 22))
        self.bottom_bar.setMaximumSize(QSize(16777215, 22))
        self.bottom_bar.setFrameShape(QFrame.NoFrame)
        self.bottom_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.credits_label = QLabel(self.bottom_bar)
        self.credits_label.setObjectName("credits_label")
        self.credits_label.setMaximumSize(QSize(16777215, 16))
        self.credits_label.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter
        )

        self.horizontalLayout_5.addWidget(self.credits_label)

        self.version = QLabel(self.bottom_bar)
        self.version.setObjectName("version")
        self.version.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottom_bar)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)

        self.verticalLayout_6.addWidget(self.bottom_bar)

        self.verticalLayout_2.addWidget(self.content_bottom)

        self.bgAppLayout.addWidget(self.content_box)

        self.styleSheetLayout.addWidget(self.bg_app)

        self.retranslateUi(case_dialog)

        QMetaObject.connectSlotsByName(case_dialog)

    # setupUi

    def retranslateUi(self, case_dialog):
        case_dialog.setWindowTitle(
            QCoreApplication.translate("case_dialog", "FIT Case", None)
        )
        self.top_logo.setText("")
        self.title_right_info.setText(
            QCoreApplication.translate("case_dialog", "Case", None)
        )
        # if QT_CONFIG(tooltip)
        self.minimize_button.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.minimize_button.setText("")
        # if QT_CONFIG(tooltip)
        self.close_button.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.close_button.setText("")
        self.temporary_msg.setText(
            QCoreApplication.translate(
                "case_dialog",
                '<html><head/><body><p><span style=" font-weight:600; text-decoration: underline; color:#fc0107;">The information is temporary and will not be saved, so once the report is generated it will be lost.</span></p></body></html>',
                None,
            )
        )
        self.temporary_name.setText("")
        self.temporary_name.setPlaceholderText(
            QCoreApplication.translate("case_dialog", "Case Name", None)
        )
        self.lawyer.setText("")
        self.lawyer.setPlaceholderText(
            QCoreApplication.translate("case_dialog", "Laywer", None)
        )
        self.operator.setText("")
        self.operator.setPlaceholderText(
            QCoreApplication.translate("case_dialog", "Operator", None)
        )
        self.courthouse.setText("")
        self.courthouse.setPlaceholderText(
            QCoreApplication.translate("case_dialog", "Courthouse", None)
        )
        self.proceeding_number.setText("")
        self.proceeding_number.setPlaceholderText(
            QCoreApplication.translate("case_dialog", "Proceeding number", None)
        )
        self.logo.setText("")
        self.logo.setPlaceholderText(
            QCoreApplication.translate("case_dialog", "Select logo", None)
        )
        self.label.setText("")
        self.logo_button.setText(
            QCoreApplication.translate("case_dialog", "Open", None)
        )
        self.notes.setPlaceholderText(
            QCoreApplication.translate("case_dialog", "Notes", None)
        )
        self.save_button.setText(
            QCoreApplication.translate("case_dialog", "Save", None)
        )
        self.cancel_button.setText(
            QCoreApplication.translate("case_dialog", "Cancel", None)
        )
        self.credits_label.setText(
            QCoreApplication.translate("case_dialog", "By: fit-project.org", None)
        )
        self.version.setText(QCoreApplication.translate("case_dialog", "v1.0.3", None))

    # retranslateUi
