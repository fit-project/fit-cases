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

    def create_acquisition_directory(self, directories):

        cases_folder = os.path.expanduser(directories.get("cases_folder"))
        if not os.path.exists(cases_folder):
            os.makedirs(cases_folder)
            os.chmod(cases_folder, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

        case_folder = os.path.join(cases_folder, directories.get("case_folder"))
        if not os.path.exists(case_folder):
            os.makedirs(case_folder)
            os.chmod(case_folder, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)

        acquisition_type_folder = os.path.join(
            case_folder, directories.get("acquisition_type_folder")
        )
        if not os.path.exists(acquisition_type_folder):
            os.makedirs(acquisition_type_folder)
            os.chmod(
                acquisition_type_folder, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO
            )

        acquisition_directory = os.path.join(acquisition_type_folder, "acquisition_1")

        if os.path.isdir(acquisition_directory):
            # Get all subdirectories from acquisition directory
            acquisition_directories = [
                d
                for d in os.listdir(acquisition_type_folder)
                if os.path.isdir(os.path.join(acquisition_type_folder, d))
            ]

            # get only directories with the right "name". This resolve issue 109
            acquisition_directories = list(
                filter(
                    lambda item: bool(re.search("^acquisition_(\d+)$", item)) == True,
                    acquisition_directories,
                )
            )

            # select the highest number in sufix name
            index = max(
                [
                    int("".join(filter(str.isdigit, item)))
                    for item in acquisition_directories
                ]
            )

            # Increment index and create the new content folder
            acquisition_directory = os.path.join(
                acquisition_type_folder, "acquisition_" + str(index + 1)
            )

        os.makedirs(acquisition_directory, exist_ok=True)

        return acquisition_directory

    def get_case_directory_list(self, cases_folder):
        subfolders = [f.name for f in os.scandir(cases_folder) if f.is_dir()]

        return subfolders
