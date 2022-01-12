# stonksbot
Discord Bot written in Python. Responds to stock symbols with quote and candlestick chart.

To use, clone this repository and run `python stonks_bot.py`
It will request a Finnhub API Key as well as a Discord Bot's token.
You can go to https://finnhub.io/ to get a Finnhub API Key and https://discord.com/developers/applications to create a Discord Bot.

The Bot responds to commands in the format of "$<\SMBL> <Time Period (Optional)>"
An example that returns simply a quote:

An example that returns candlestick charts over a time period (can replace argument with "d" (day), "w" (week), "m" (month), "y" (year) or a number (in hours) of history to display.
