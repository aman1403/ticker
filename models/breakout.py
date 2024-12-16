from typing import Optional

class Breakout:
    """
    Represents a breakout point in stock data.
    """
    def __init__(
        self,
        breakout_date: str,
        breakout_day_open: float,
        breakout_day_close: float,
        volume_on_breakout_day: int,
        avg_volume_last_20_days: float,
        currency: str,  
        date_after_20_days: Optional[str] = None,
        price_after_20_days: Optional[float] = None,
        return_percentage: Optional[float] = None
    ):
        self.breakout_date = breakout_date
        self.breakout_day_open = breakout_day_open
        self.breakout_day_close = breakout_day_close
        self.volume_on_breakout_day = volume_on_breakout_day
        self.avg_volume_last_20_days = avg_volume_last_20_days
        self.currency = currency 
        self.date_after_20_days = date_after_20_days or "Data Not Available"
        self.price_after_20_days = price_after_20_days or "Data Not Available"
        self.return_percentage = (
            round(return_percentage, 2) if return_percentage is not None else "Data Not Available"
        )

    def to_dict(self) -> dict:
        """
        Converts the Breakout object to a dictionary.
        """
        return {
            "Breakout Date": self.breakout_date,
            "Breakout Day Open": self.breakout_day_open,
            "Breakout Day Close": self.breakout_day_close,
            "Volume on Breakout Day": self.volume_on_breakout_day,
            "Average Volume (Last 20 Days)": self.avg_volume_last_20_days,
            "Currency": self.currency,  
            "Date After 20 Days": self.date_after_20_days,
            "Price After 20 Days": self.price_after_20_days,
            "Return (%)": self.return_percentage,
        }

    def __repr__(self) -> str:
        return f"Breakout({self.to_dict()})"
