import pandas as pd
import yfinance as yf
import numpy as np
import datetime

# different price frequencies are required depending on the assessment
# up to 200 day history with interval of 1-day is required for SMAs/RSI
# single data points with interval of 1-hour for current price check


class Assets:
    """
    Has been designed only considering NYSE and Nasdaq stock market times.
    """
    def __init__(self, tickers):
        self.tickers = tickers
        self.today = datetime.date.today()
        self.delta_300day = self.today - datetime.timedelta(300)
        self.delta_5day = self.today - datetime.timedelta(5)

    def get_current_price(self):
        """
        Get current price of initialized tickers
        :return:
        current_prices: dictionary containing ticker and corresponding
                        tuple of last available date and price.
        """
        current_prices = {}
        for ticker in self.tickers:
            ticker_object = yf.Ticker(ticker)
            # collect 5-day historical data
            ticker_history = ticker_object.history(start=self.delta_5day,
                                                   end=self.today,
                                                   interval="1m")
            # adjust columns
            ticker_history.index.name = "Date"
            ticker_history.reset_index(inplace=True)
            # store only date and close price
            close_stock_history = ticker_history[["Date", "Close"]].copy()
            latest_date = close_stock_history["Date"].iloc[-1]
            latest_price = close_stock_history["Close"].iloc[-1]
            latest_price_tuple = (latest_date, latest_price)
            current_prices[ticker] = latest_price_tuple

        return current_prices

    def is_latest(self):
        """
        Returns True if latest price is current day, False otherwise.

        :return:
        check: (boolean)
        """
        pass

    def get_long(self):
        """Get 200 days worth of stock/crypto data for provided ticker
        symbols, during initialization.

        :param
        None

        :return
        data: DataFrame table containing 200-days worth of price-close
              data for each ticker.
        """
        # dictionary to store ticker and dataframe of ticker close price
        price_data = {}

        for ticker in self.tickers:
            ticker_object = yf.Ticker(ticker)
            # collect 200-day historical data
            ticker_history = ticker_object.history(start=self.delta_300day,
                                                   end=self.today,
                                                   interval="1d")
            # adjust columns
            ticker_history.index.name = "Date"
            ticker_history.reset_index(inplace=True)
            # store only date and close price
            close_stock_history = ticker_history[["Date", "Close"]].copy()
            # update dictionary
            price_data[ticker] = close_stock_history

        # combine price_data entries into single entry
        price_data = {k: v.set_index('Date') for k, v in price_data.items()}
        price_df = pd.concat(price_data, axis=1)
        price_df.columns = price_df.columns.droplevel(-1)

        return price_df

    def moving_average(self, days):
        """
        Function calculates the requested SMA. The function uses
        self.ticker and get_long function to get the information for the
        calculation.

        :param:
        days: amount of days to calculate the SMA. Limited to around
              210 days due to how the class is initialized. Values above
              200 will be converted to 200.

        :return:
        moving_averages: dictionary of tickers and corresponding SMA
        """
        if days > 200:
            days = 200
        price_df = self.get_long()
        moving_averages = {}
        for ticker in self.tickers:
            moving_average = price_df[ticker].rolling(days).mean()[-1]
            moving_averages[ticker] = moving_average

        return moving_averages


ticker_list = ["aapl", "tsla"]
alert = Assets(ticker_list)
curr_price = alert.get_current_price()
ma_50 = alert.moving_average(50)
ma_200 = alert.moving_average(200)
print(f"{curr_price}\n{ma_50.items()}\n{ma_200.items()}")
ts = pd.Timestamp(curr_price[ticker_list[0]][0])
ts = ts.to_datetime64()
print(ts, datetime.datetime.now())
# print(ts == datetime.date.today())
