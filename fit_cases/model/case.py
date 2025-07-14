#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


from fit_cases.model.db import Db

import os
import stat
import re

from sqlalchemy import Column, Integer, String, Text, LargeBinary
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Case(Base):
    __tablename__ = "cases"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    lawyer_name = Column(String)
    operator = Column(String)
    proceeding_type = Column(Integer)
    courthouse = Column(String)
    proceeding_number = Column(Integer)
    notes = Column(Text)
    logo_bin = Column(LargeBinary)
    logo = Column(String)
    logo_height = Column(String)
    logo_width = Column(String)

    def __init__(self) -> None:
        super().__init__()
        self.db = Db()
        self.metadata.create_all(self.db.engine)

    def get(self):
        return self.db.session.query(Case).all()

    def get_from_id(self, id):
        return self.db.session.query(Case).filter_by(id=id).one()

    def update(self, case_info):
        if os.path.isfile(case_info.get("logo")):
            case_info["logo_bin"] = self.__set_logo_bin(case_info.get("logo"))

        self.db.session.query(Case).filter(Case.id == case_info.get("id")).update(
            case_info
        )
        self.db.session.commit()

    def add(self, case_info):
        case = Case()
        case.name = case_info.get("name")
        case.lawyer_name = case_info.get("lawyer_name")
        case.operator = case_info.get("operator")
        case.proceeding_type = case_info.get("proceeding_type")
        case.courthouse = case_info.get("courthouse")
        case.proceeding_number = case_info.get("proceeding_number")
        case.notes = case_info.get("notes")
        case.logo = case_info.get("logo")
        case.logo_height = case_info.get("logo_height")
        case.logo_width = case_info.get("logo_width")
        if os.path.isfile(case.logo):
            case.logo_bin = self.__set_logo_bin(case.logo)

        self.db.session.add(case)
        self.db.session.commit()

        return self.db.session.query(Case).order_by(Case.id.desc()).first()

    def __set_logo_bin(self, file_path):
        with open(file_path, "rb") as file:
            return file.read()
