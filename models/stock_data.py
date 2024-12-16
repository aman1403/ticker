from datetime import datetime
from typing import Dict

class StockData:
    """
    Represents a single day's stock data, including UTC date as an integer.
    """
    def __init__(
        self,
        date: str,
        utc_date: int,
        open_price: float,
        high_price: float,
        low_price: float,
        close_price: float,
        volume: int
    ):
        """
        Initializes a StockData instance.

        Parameters:
            date (str): The date in YYYY-MM-DD format.
            utc_date (int): The UTC timestamp as an integer.
            open_price (float): The opening price of the stock.
            high_price (float): The highest price of the stock.
            low_price (float): The lowest price of the stock.
            close_price (float): The closing price of the stock.
            volume (int): The trading volume of the stock.
        """
        self.date = date
        self.utc_date = int(utc_date)
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume

    @classmethod
    def from_dict(cls, data: Dict[str, float]) -> "StockData":
        """
        Creates a StockData instance from a dictionary.

        Parameters:
            data (Dict[str, float]): A dictionary containing stock data.

        Returns:
            StockData: An instance of the StockData class.
        """
        return cls(
            date=data["date"],
            utc_date=int(data["date_utc"]),
            open_price=float(data["open"]),
            high_price=float(data["high"]),
            low_price=float(data["low"]),
            close_price=float(data["close"]),
            volume=int(data["volume"]),
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the StockData object.

        Returns:
            str: A string representation of the object.
        """
        return (
            f"StockData(date={self.date}, utc_date={self.utc_date}, readable_utc_date={self.readable_utc_date}, "
            f"open={self.open_price}, high={self.high_price}, low={self.low_price}, close={self.close_price}, volume={self.volume})"
        )
