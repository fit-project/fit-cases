#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from fit_cases.model.case import Case as CaseModel


class Case:
    _cases = []
    _names = []

    def __init__(self):
        self.model = CaseModel()
        self.__load_cases()
        self._keys = self.model.metadata.tables["cases"].columns.keys()

    def __load_cases(self):
        cases = self.model.get()

        self._cases.clear()
        self._names.clear()

        for i in range(len(cases)):
            self._cases.append(
                {
                    key: value
                    for key, value in cases[i].__dict__.items()
                    if not key.startswith("_")
                    and not key.startswith("__")
                    and not key.startswith("db")
                }
            )
            self._names.append(
                {
                    key: value
                    for key, value in cases[i].__dict__.items()
                    if key == "name"
                }
            )

    @property
    def keys(self):
        return self._keys

    @property
    def cases(self):
        return self._cases

    @cases.setter
    def cases(self, case_info):
        self.model.update(case_info)
        self.__load_cases()

    def add(self, case_info):
        case_info = self.model.add(case_info)
        self.__load_cases()
        return {
            key: value
            for key, value in case_info.__dict__.items()
            if not key.startswith("_")
            and not key.startswith("__")
            and not key.startswith("db")
        }

    @property
    def names(self):
        return list(map(lambda x: x["name"], self._names))
