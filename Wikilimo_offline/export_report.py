# Using credentials to create a client to interact with the Google Sheets API
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open("Wikilimo Citizen Science Report").sheet1


def get_latest_pest(sheet):
    col = sheet.col_values(3)
    return col[-1]


def get_latest_contact(sheet):
    col = sheet.col_values(4)
    return col[-1]
