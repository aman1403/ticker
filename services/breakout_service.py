from collections import deque
from typing import List
from models.stock_data import StockData
from models.breakout import Breakout

class BreakoutService:
    """
    Service for identifying breakout points and calculating returns from stock data.
    """
    def __init__(self, volume_threshold: float, price_threshold: float):
        self.volume_threshold = volume_threshold
        self.price_threshold = price_threshold

    def identify_breakouts(self, stock_data: List[StockData], currency: str) -> List[Breakout]:
        """
        Identifies breakout points and calculates returns.

        Parameters:
            stock_data (List[StockData]): A list of StockData objects sorted by date.

        Returns:
            List[Breakout]: A list of Breakout objects containing breakout details.
        """
        last_20_volumes = deque(maxlen=20)  # Store the last 20 volumes
        breakouts = []
        previous_close = None  # To keep track of yesterday's close price

        for i, stock in enumerate(stock_data):
            if len(last_20_volumes) < 20:
                last_20_volumes.append(stock.volume)
                previous_close = stock.close_price  # Update previous day's close price
                continue

            # Calculate average volume over the last 20 days
            avg_volume = sum(last_20_volumes) / 20

            # Check breakout conditions (pass previous day's close price)
            if self._is_breakout(stock, avg_volume, previous_close):
                price_after_20_days, return_pct = self._calculate_return(stock_data, i)

                # Create a Breakout object
                breakout = Breakout(
                    breakout_date=stock.date,
                    breakout_day_open=stock.open_price,
                    breakout_day_close=stock.close_price,
                    volume_on_breakout_day=stock.volume,
                    avg_volume_last_20_days=avg_volume,
                    currency=currency,
                    date_after_20_days=price_after_20_days["date"] if price_after_20_days else None,
                    price_after_20_days=price_after_20_days["price"] if price_after_20_days else None,
                    return_percentage=return_pct,
                )
                breakouts.append(breakout)

            # Add current day's volume to the deque and update previous day's close price
            last_20_volumes.append(stock.volume)
            previous_close = stock.close_price

        return breakouts

    def _is_breakout(self, stock: StockData, avg_volume: float, previous_close: float) -> bool:
        """
        Determines whether the current day qualifies as a breakout.

        Parameters:
            stock (StockData): The current day's stock data.
            avg_volume (float): Average volume over the last 20 days.
            previous_close (float): The previous day's close price.

        Returns:
            bool: True if breakout conditions are met, False otherwise.
        """
        if previous_close is None or previous_close == 0:
            return False
    
        return (
            stock.volume > self.volume_threshold * avg_volume and
            (stock.close_price - previous_close) / previous_close >= self.price_threshold
        )

    def _calculate_return(self, stock_data: List[StockData], index: int) -> tuple:
        """
        Calculates the return percentage after 20 days from the breakout point.

        Parameters:
            stock_data (List[StockData]): List of stock data.
            index (int): Current index of the breakout.

        Returns:
            tuple: A dictionary with date and price after 20 days, and return percentage.
        """
        if index + 20 < len(stock_data):
            future_stock = stock_data[index + 20]
            return_pct = ((future_stock.close_price - stock_data[index].close_price) / stock_data[index].close_price) * 100
            return {"date": future_stock.date, "price": future_stock.close_price}, return_pct
        return None, None
