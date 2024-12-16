# services/yahoo_finance_service.py

import requests
from config.constants import YAHOO_FINANCE_BASE_URL, YAHOO_FINANCE_HOST
from models.stock_summary import StockSummary

class YahooFinanceService:
    """
    Service to interact with the Yahoo Finance API for fetching stock data.
    """
    def __init__(self, api_key: str):
        """
        Initializes the YahooFinanceService.

        Parameters:
            api_key (str): API key for authenticating Yahoo Finance API requests.
        """
        self.api_key = api_key
        self.base_url = YAHOO_FINANCE_BASE_URL
        self.headers = {
            "x-rapidapi-host": YAHOO_FINANCE_HOST,
            "x-rapidapi-key": self.api_key,
        }

    def fetch_stock_data(self, ticker: str, interval: str = "1d") -> StockSummary:
        """
        Fetches stock data and metadata for the given ticker.

        Parameters:
            ticker (str): The stock ticker symbol (e.g., "TSLA").
            interval (str): The time interval for the data (default: "1d").

        Returns:
            StockSummary: An object containing metadata and stock data.
        """
        params = {
            "symbol": ticker,
            "interval": interval,
            "diffandsplits": "false",
        }

        # Make the API request
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the JSON response
        data = response.json()

        # Handle API-specific errors or missing data
        if not data.get("success", True):
            raise ValueError(f"Error fetching data for ticker {ticker}: {data.get('message', 'Unknown error')}")

        # Map the response to the StockSummary object
        stock_summary = StockSummary.from_api_response(data)

        return stock_summary
