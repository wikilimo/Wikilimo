import pytest
from export_report import sheet


def test_sheet_loaded():
    """ TODO: Smoke test to ensure correct worksheet loaded from spreadsheet """


def test_get_latest_pest(sheet):
    assert "Pest infestation observed (if any)?" == sheet.cell(1, 3).value


def test_get_latest_contact(sheet):
    assert "Enter your phone number to be notified of severe weather and/or pest infestations nearby." \
           == sheet.cell(1, 4).value
