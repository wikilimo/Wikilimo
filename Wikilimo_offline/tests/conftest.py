"""Global test configuration and shared fixtures"""

import pytest
import gspread
from oauth2client.service_account import ServiceAccountCredentials

@pytest.fixture
def sheet():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive.file',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Wikilimo Citizen Science Report").sheet1

    return sheet


@pytest.fixture
def location():
    return location