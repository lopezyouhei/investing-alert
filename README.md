# Investing Alert

The script takes in ticker markers from user-defined stock and/or crypto
(yfinance) and sends out an email to the given email address when one of 
the following criteria are met:

1. The stock/crypto price falls below the 50 and 200 SMA.
2. The stock/crypto RSI is below 30.

## Output
The email will be formatted with which criteria was met. If both are met,
the alert is "strong", otherwise it is just a simple alert. Of course, 
"strong" is extremely subjective to which company was chosen, market 
conditions, even the alert criteria. 

## Strategy
The objective of this alert is to support a long term investment 
portfolio of large cap-dividend paying companies, with stable/growing 
business activities. The idea is to take advantage of market cycles to 
buy company stocks at a superficially higher dividend yield. 

### Disclaimer
This is just meant to be a project where I can learn how to program 
something which interests me and that I do on a daily basis manually.
I am not a financial advisor in any way. If you plan to use this script,
do so at your own risk.