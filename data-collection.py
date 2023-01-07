import pandas as pd
import yfinance as yf
import numpy as np

# different price frequencies are required depending on the assessment
# up to 200 day history with interval of 1-day is required for SMAs/RSI
# single data points with interval of 1-hour for current price check


class Assets:

    def __init__(self, tickers):
        self.tickers = tickers

    def get_long(self):
        pass
