from __future__ import annotations

import sys

import pytest
from PySide6.QtWidgets import QDialog

import main as fit_cases_main


@pytest.mark.unit
def test_parse_args_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(sys, "argv", ["fit-cases"])

    args = fit_cases_main.parse_args()

    assert args.debug == "none"


@pytest.mark.unit
def test_main_sets_debug_level_and_handles_accept(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(fit_cases_main, "parse_args", lambda: type("Args", (), {"debug": "verbose"})())

    calls: dict[str, list] = {"set_debug_level": [], "debug": []}

    monkeypatch.setattr(
        fit_cases_main,
        "set_debug_level",
        lambda value: calls["set_debug_level"].append(value),
    )
    monkeypatch.setattr(
        fit_cases_main,
        "debug",
        lambda message, context=None: calls["debug"].append((message, context)),
    )

    class FakeApp:
        def __init__(self, argv):
            self.argv = argv

    class FakeDialog:
        def exec(self):
            return QDialog.Accepted

    monkeypatch.setattr(fit_cases_main, "QApplication", FakeApp)
    monkeypatch.setattr(fit_cases_main, "CaseFormDialog", FakeDialog)

    rc = fit_cases_main.main()

    assert rc == 0
    assert calls["set_debug_level"] == [fit_cases_main.DebugLevel.VERBOSE]
    assert calls["debug"] == [
        ("ℹ️ User accepted the case form", "main.fit_cases")
    ]
