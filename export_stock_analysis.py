import gspread
from oauth2client.service_account import ServiceAccountCredentials
from services.stock_analysis_service import get_breakout_points
from utils.data_processing import DataProcessor
from config.constants import GOOGLE_SCOPES, GOOGLE_SHEET_NAME

class GoogleSheetsManager:
    def __init__(self, credentials_file: str, spreadsheet_name: str):
        """
        Initializes the Google Sheets Manager.

        Parameters:
            credentials_file (str): Path to the Google credentials JSON file.
            spreadsheet_name (str): Name of the Google Spreadsheet.
        """
        self.spreadsheet_name = spreadsheet_name
        self.scope = GOOGLE_SCOPES
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, self.scope)
        self.client = gspread.authorize(self.credentials)
        self.spreadsheet = self._get_or_create_spreadsheet()

    def _get_or_create_spreadsheet(self):
        """
        Retrieves the spreadsheet by name or creates a new one if it doesn't exist.
        """
        try:
            return self.client.open(self.spreadsheet_name)
        except gspread.SpreadsheetNotFound:
            return self.client.create(self.spreadsheet_name)

    def create_or_update_worksheet(self, ticker: str, breakout_data: list):
        """
        Creates or updates a worksheet for the given ticker with breakout data.

        Parameters:
            ticker (str): The stock ticker name.
            breakout_data (list): A list of breakout dictionaries to write to the sheet.
        """
        try:
            # Delete the worksheet if it already exists
            worksheet = self.spreadsheet.worksheet(ticker)
            self.spreadsheet.del_worksheet(worksheet)
        except gspread.WorksheetNotFound:
            pass

        # Create a new worksheet
        worksheet = self.spreadsheet.add_worksheet(title=ticker, rows="100", cols="10")

        # Write data
        if breakout_data:
            headers = breakout_data[0].keys()
            worksheet.append_row(list(headers))
            for row in breakout_data:
                worksheet.append_row(list(row.values()))
            print(f"Breakout data written for {ticker}.")
        else:
            worksheet.append_row(["No breakout points found."])
            print(f"No breakout points for {ticker}.")

def read_tickers(file_path: str) -> list:
    """
    Reads stock tickers from a file.

    Parameters:
        file_path (str): Path to the tickers.txt file.

    Returns:
        list: A list of uppercase ticker symbols.
    """
    try:
        with open(file_path, "r") as f:
            return [line.strip().upper() for line in f.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: {file_path} not found in the root directory.")

def process_tickers(tickers: list, sheets_manager: GoogleSheetsManager):
    """
    Processes a list of tickers, retrieves breakout points, and writes to Google Sheets.

    Parameters:
        tickers (list): List of stock tickers.
        sheets_manager (GoogleSheetsManager): Instance of GoogleSheetsManager to handle Sheets operations.
    """
    for ticker in tickers:
        try:
            # Get breakout points
            breakouts = get_breakout_points(ticker)
            breakout_data = [breakout.to_dict() for breakout in breakouts]
            sheets_manager.create_or_update_worksheet(ticker, breakout_data)
        except Exception as e:
            print(f"Error processing ticker {ticker}: {e}")

def main():
    credentials_file = "credentials.json"
    tickers_file = "tickers.txt"

    try:
        # Initialize Google Sheets Manager
        sheets_manager = GoogleSheetsManager(credentials_file, GOOGLE_SHEET_NAME)

        # Read tickers from file
        tickers = read_tickers(tickers_file)

        # Process tickers and write data to Google Sheets
        process_tickers(tickers, sheets_manager)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
