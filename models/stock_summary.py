from typing import Dict, List
from models.stock_data import StockData

class StockSummary:
    """
    Represents a summary of stock data, including metadata such as currency.
    """
    def __init__(self, currency: str, stock_data: List[StockData]):
        """
        Initializes the StockSummary instance.

        Parameters:
            currency (str): The currency in which stock prices are listed.
            stock_data (List[StockData]): A list of StockData objects.
        """
        self.currency = currency
        self.stock_data = stock_data

    @classmethod
    def from_api_response(cls, response: Dict) -> "StockSummary":
        """
        Creates a StockSummary instance from an API response.

        Parameters:
            response (Dict): The API response containing metadata and stock data.

        Returns:
            StockSummary: An instance of the StockSummary class.
        """
        # Extract currency from the metadata
        currency = response["meta"].get("currency", "Unknown Currency")

        # Parse stock data from the body
        stock_data = [
            StockData.from_dict(entry)
            for entry in response["body"].values()
        ]

        return cls(currency=currency, stock_data=stock_data)

    def __repr__(self) -> str:
        """
        Returns a string representation of the StockSummary object.

        Returns:
            str: A string representation of the object.
        """
        return f"StockSummary(currency={self.currency}, stock_data=[...])"
