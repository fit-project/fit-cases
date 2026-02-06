#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

import argparse
import sys

from fit_common.core import DebugLevel, debug, set_debug_level
from PySide6.QtWidgets import QApplication, QDialog

from fit_cases.view.case_form_dialog import CaseFormDialog


def parse_args():
    parser = argparse.ArgumentParser(description="FIT Web Module")
    parser.add_argument(
        "--debug",
        choices=["none", "log", "verbose"],
        default="none",
        help="Set the debug level (default: none)",
    )
    return parser.parse_args()


def main():

    args = parse_args()
    set_debug_level(
        {
            "none": DebugLevel.NONE,
            "log": DebugLevel.LOG,
            "verbose": DebugLevel.VERBOSE,
        }[args.debug]
    )

    app = QApplication(sys.argv)
    window = CaseFormDialog()

    result = window.exec()
    if result == QDialog.Accepted:
        debug("ℹ️ User accepted the case form", context="main.fit_cases")
    else:
        debug(
            "❌ User cancelled the case form. Nothing to display.",
            context="main.fit_cases",
        )

    return 0


if __name__ == "__main__":
    main()
