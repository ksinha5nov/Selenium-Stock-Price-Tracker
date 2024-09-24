# Stock Price Scraper using Selenium

This project is a Python-based web scraper that uses Selenium to extract real-time stock price data from Yahoo Finance. The scraper navigates to the stock pages of specified companies and extracts the current stock price by accessing the `data-value` attribute from the HTML structure.

## Features:
- Fetches real-time stock prices from Yahoo Finance for a list of specified stocks.
- Bypasses SSL certificate warnings using Chrome WebDriver options.
- Extracts the stock price from the `data-value` attribute in the `fin-streamer` element for accurate data retrieval.
- Saves the scraped data (stock name and price) to a CSV file for further analysis or reporting.

## Technologies Used:
- Python
- Selenium
- Pandas
- Chrome WebDriver

## Usage:
1. Install the required dependencies:
   ```bash
   pip install selenium pandas

2. Download the Chrome WebDriver and ensure it's available in your system's PATH or set the correct path in the script.
3. Run the script to automatically fetch stock data and save it to a CSV file:
   ```bash
   python stock_scraper.py
4. Customize the list of stock symbols in the script to target different companies.
