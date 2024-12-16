# Breakout Points Analyzer

## Overview
This application is designed to provide insights into stock market data like breakout dates via a user-friendly interface. Additionally, it allows exporting stock analysis data into Google Sheets for further processing.

## Features
- Interactive UI for stock analysis and visualization.
- Integration with Yahoo Finance for stock data.
- Export data to Google Sheets for analysis.

## Prerequisites
Before starting, ensure you have the following:

1. **Yahoo Finance API Key**: Required for fetching stock data.
2. **Google Sheets Credentials**: Necessary for exporting data to Google Sheets.

## Getting Started

### Step 1: Obtain Yahoo Finance API Key
1. Go to the YH Finance API page on [RapidAPI](https://rapidapi.com/sparior/api/yahoo-finance15).
2. Click on the "Sign Up" button if you don’t have a RapidAPI account, or "Login" if you already have an account.
3. Once logged in, click on the "Subscribe to Test" button to subscribe to the free plan or a paid plan based on your requirements.
4. Navigate to the "Endpoints" tab and locate the "X-RapidAPI-Key" field. This is your API key.
5. Copy the API key and store it securely.

### Step 2: Set Up Google Sheets Credentials
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the Google Sheets API.
3. Generate service account credentials in JSON format.
4. Download the `credentials.json` file and place it in the root directory of the project.

### Step 3: Clone the Repository
```bash
# Clone the repository
$ git clone <repository-url>

# Navigate to the project directory
$ cd ticker
```

### Step 4: Set Up a Virtual Environment
```bash
#Create the virtual environment:
python3 -m venv venv

#Activate the virtual environment:
#For macOS/Linux:
source venv/bin/activate

#For Windows:
venv\Scripts\activate

#Install Dependencies
# Install the required Python libraries
$ pip install -r requirements.txt
```

### Step 5: Set Up Environment Variables
1. Create a `.env` file in the root directory.
2. Add the following environment variables:
   ```env
   YAHOO_FINANCE_API_KEY=<your_api_key>
   ```

## Usage

### Interactive Stock Analysis
1. Start the Streamlit application:
   ```bash
   $ streamlit run app.py
   ```
2. In the UI:
   - Provide a stock ticker symbol (e.g., `AAPL` for Apple Inc.).
   - View breakout dates and return graph for the given ticker.

### Export Stock Data to Google Sheets
1. Ensure the `credentials.json` file is present in the root directory.
2. Set the Google Sheet name in `config/constants.py`:
   ```python
   GOOGLE_SHEET_NAME = "Your Google Sheet Name"
   ```
3. Add the desired ticker symbols to `tickers.txt` (one ticker per line).
4. Run the export script:
   ```bash
   $ python3 export_stock_analysis.py
   ```
5. The data will be exported to the specified Google Sheet.

## Project Structure
```
.
├── app.py                     # Main application entry point.
├── requirements.txt           # Dependencies for the project.
├── .env                       # Environment variables (not included).
├── credentials.json           # Google Sheets API credentials (not included).
├── tickers.txt                # List of stock tickers for analysis.
├── export_stock_analysis.py   # Script to export data to Google Sheets.
├── config/
│   ├── constants.py           # Constants for the application.
│   └── settings.py            # Configuration settings.
├── utils/
│   └── data_processing.py     # Utility functions for data processing.
├── models/
│   ├── breakout.py            # Logic for breakout analysis.
│   ├── stock_data.py          # Logic for stock data processing.
│   └── stock_summary.py       # Logic for summarizing stock data.
├── services/
│   ├── stock_analysis_service.py   # Service for stock analysis.
│   ├── breakout_service.py         # Service for breakout calculations.
│   └── yahoo_finance_service.py   # Service for Yahoo Finance API.
```

## Notes
- Keep `.env` and `credentials.json` files in the root directory as mentioned above.
- Ensure proper permissions are granted to the Google Sheets service account.

