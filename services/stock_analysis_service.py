from config.settings import api_key
from config.constants import VOLUME_THRESHOLD, PRICE_THRESHOLD
from services.yahoo_finance_service import YahooFinanceService
from services.breakout_service import BreakoutService
from utils.data_processing import DataProcessor
from models.breakout import Breakout
from models.stock_summary import StockSummary
from typing import List

def get_breakout_points(ticker: str) -> List[Breakout]:
    """
    Fetches stock data, processes it, and identifies breakout points.

    Parameters:
        ticker (str): The stock ticker to analyze (e.g., "NVDA").

    Returns:
        List[Breakout]: A list of breakout objects.
    """
    try:
        # Fetch stock summary (includes metadata and stock data)
        yahoo_service = YahooFinanceService(api_key)
        stock_summary = yahoo_service.fetch_stock_data(ticker)

        # Extract stock data and sort it
        sorted_stock_data = DataProcessor.sort_stock_data_by_date(stock_summary.stock_data)

        # Identify breakout points
        breakout_service = BreakoutService(
            volume_threshold=VOLUME_THRESHOLD,
            price_threshold=PRICE_THRESHOLD
        )
        breakouts = breakout_service.identify_breakouts(sorted_stock_data, stock_summary.currency)

        return breakouts

    except ValueError as e:
        raise ValueError(f"Failed to fetch or process data for {ticker}: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred for {ticker}: {e}")
