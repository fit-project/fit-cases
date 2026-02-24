#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_cases.view.case_form_dialog import CaseFormDialog


def show_case_info_dialog(case_info):
    CaseFormDialog(case_info).exec()
