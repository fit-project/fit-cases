#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6.QtWidgets import QApplication
import sys

from fit_cases.view.case_form_dialog import CaseFormDialog


def main():
    app = QApplication(sys.argv)
    window = CaseFormDialog()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
