import pandas as pd
import yfinance as yf
import numpy as np
import datetime

# different price frequencies are required depending on the assessment
# up to 200 day history with interval of 1-day is required for SMAs/RSI
# single data points with interval of 1-hour for current price check


class Assets:

    def __init__(self, tickers):
        self.tickers = tickers

    def get_long(self):
        """Get 200 days worth of stock/crypto data for provided ticker
        symbols, during initialization.

        :param
        None

        :return
        data: DataFrame table containing 200-days worth of price-close
              data for each ticker.
        """
        price_data = {}
        for ticker in self.tickers:
            ticker_object = yf.Ticker(ticker)
            ticker_close_price = ticker_object.history(start=datetime.date.today(),
                                                       end=)
            ticker_close_price = [["Date",
                                   "Open",
                                   "High",
                                   "Low",
                                   "Close"]].copy()


ticker_list = ["aapl"]
alert = Assets(ticker_list)
print(alert)