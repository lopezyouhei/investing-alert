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
        self.today = datetime.date.today()
        self.delta_200day = self.today - datetime.timedelta(200)

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
            ticker_history = ticker_object.history(start=self.delta_200day,
                                                   end=self.today,
                                                   interval="1d")
            ticker_history.index.name = "Date"
            ticker_history.reset_index(inplace=True)
            close_stock_history = ticker_history[["Date", "Close"]].copy()
            price_data[ticker] = close_stock_history

            price_data = {k: v.set_index('Date') for k, v in price_data.items()}
            price_df = pd.concat(price_data, axis=1)
            price_df.columns = price_df.columns.droplevel(-1)
        return price_df


ticker_list = ["aapl", "tsla"]
alert = Assets(ticker_list)
print(alert)