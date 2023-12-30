import os
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def open_spreadsheet(client_secret, spreadsheet_title):
    try:
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(client_secret, scope)
        client = gspread.authorize(creds)
        return client.open(spreadsheet_title)
    except Exception as e:
        print(f"Error opening spreadsheet: {e}")
        return None


def write_worksheet_to_csv(worksheet, name, csv_dir):
    try:
        file_path = os.path.join(csv_dir, f'{name}.csv')
        with open(file_path, 'w', newline='', encoding='utf-8') as obj:
            writer = csv.writer(obj)
            writer.writerows(worksheet.get_all_values())
        print(f'Successfully written {name} to CSV.')
    except Exception as e:
        print(f"Error writing {name} to CSV: {e}")


def download(client_secret, spreadsheet_title, sheets, output_dir):
    print("Begin download of Google Spreadsheet...")
    sh = open_spreadsheet(client_secret, spreadsheet_title)

    if sh is None:
        print(f"Failed to open spreadsheet {spreadsheet_title}")
        return

    for name in sheets:
        try:
            worksheet = sh.worksheet(name)
            write_worksheet_to_csv(worksheet, name, output_dir)
        except Exception as e:
            print(f"Error processing sheet {name}: {e}")
