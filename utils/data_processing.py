# utils/data_processing.py

import pandas as pd
from typing import List
from models.stock_data import StockData

class DataProcessor:
    @staticmethod
    def sort_stock_data_by_date(stock_data: List[StockData]) -> List[StockData]:
        """
        Sorts stock data by the `utc_date` field.

        Parameters:
            stock_data (List[StockData]): List of StockData objects.

        Returns:
            List[StockData]: Sorted list of StockData objects.
        """
        return sorted(stock_data, key=lambda x: x.utc_date)

    @staticmethod
    def format_breakout_data(breakout_rows: List[dict]) -> pd.DataFrame:
        """
        Formats breakout data into a DataFrame.

        Parameters:
            breakout_rows (List[dict]): List of dictionaries representing breakout data.

        Returns:
            pd.DataFrame: A DataFrame containing the breakout data.
        """
        if not breakout_rows:
            return pd.DataFrame()  # Return an empty DataFrame if no data is provided

        return pd.DataFrame(breakout_rows)

    @staticmethod
    def convert_stock_data_to_dataframe(stock_data: List[StockData]) -> pd.DataFrame:
        """
        Converts a list of StockData objects to a Pandas DataFrame.

        Parameters:
            stock_data (List[StockData]): List of StockData objects.

        Returns:
            pd.DataFrame: A DataFrame containing the stock data.
        """
        if not stock_data:
            return pd.DataFrame()  # Return an empty DataFrame if no data is provided

        return pd.DataFrame([{
            "Date": stock.date,
            "UTC Date": stock.utc_date,
            "Open": stock.open_price,
            "High": stock.high_price,
            "Low": stock.low_price,
            "Close": stock.close_price,
            "Volume": stock.volume
        } for stock in stock_data])
