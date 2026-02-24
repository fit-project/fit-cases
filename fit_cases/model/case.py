#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


from typing import Any
import os

from sqlalchemy import Integer, LargeBinary, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from fit_cases.model.db import Db


class Base(DeclarativeBase):
    pass


class Case(Base):
    __tablename__ = "cases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str | None] = mapped_column(String, unique=True)
    lawyer_name: Mapped[str | None] = mapped_column(String)
    operator: Mapped[str | None] = mapped_column(String)
    proceeding_type: Mapped[int | None] = mapped_column(Integer)
    courthouse: Mapped[str | None] = mapped_column(String)
    proceeding_number: Mapped[int | None] = mapped_column(Integer)
    notes: Mapped[str | None] = mapped_column(Text)
    logo_bin: Mapped[bytes | None] = mapped_column(LargeBinary)
    logo: Mapped[str | None] = mapped_column(String)
    logo_height: Mapped[str | None] = mapped_column(String)
    logo_width: Mapped[str | None] = mapped_column(String)

    def __init__(self) -> None:
        super().__init__()
        self.db = Db()
        self.metadata.create_all(self.db.engine)

    def get(self):
        return self.db.session.query(Case).all()

    def get_from_id(self, id):
        return self.db.session.query(Case).filter_by(id=id).one()

    def update(self, case_info: dict[str, Any]) -> None:
        logo_path = case_info.get("logo")
        if isinstance(logo_path, str) and os.path.isfile(logo_path):
            case_info["logo_bin"] = self.__set_logo_bin(logo_path)

        self.db.session.query(Case).filter(Case.id == case_info.get("id")).update(
            case_info
        )
        self.db.session.commit()

    def add(self, case_info: dict[str, Any]) -> "Case":
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
        if case.logo and os.path.isfile(case.logo):
            case.logo_bin = self.__set_logo_bin(case.logo)

        self.db.session.add(case)
        self.db.session.commit()

        return self.db.session.query(Case).order_by(Case.id.desc()).first()

    def __set_logo_bin(self, file_path: str) -> bytes:
        with open(file_path, "rb") as file:
            return file.read()
