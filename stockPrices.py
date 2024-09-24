from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Set up Chrome options to ignore SSL certificate errors
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# Set up WebDriver with Service
chrome_service = Service("C:\\Drivers\\chromedriver-win64\\chromedriver.exe")  # Update this path with your actual chromedriver location
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Function to scrape stock data
def scrape_stock_data():
    stocks = ["AAPL", "GOOGL", "TSLA", "SONY"]  # List of stocks to scrape
    stock_data = []

    for stock in stocks:
        # Navigate to the stock page
        url = f"https://finance.yahoo.com/quote/{stock}?p={stock}&.tsrc=fin-srch"
        driver.get(url)

        # Wait for the stock name using its class name
        try:
            stock_name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'yf-vfa1ac'))
            ).text
        except Exception as e:
            print(f"Error fetching stock name for {stock}: {e}")
            stock_name = "N/A"

        # Wait for the stock price using CSS selector targeting `class="livePrice yf-1i5aalm"`
        try:
            stock_price = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'fin-streamer[class="livePrice yf-1i5aalm"]'))
            ).get_attribute("data-value")
        except Exception as e:
            print(f"Error fetching stock price for {stock}: {e}")
            stock_price = "N/A"
        
        # Append data to stock_data list
        stock_data.append({
            'Stock': stock_name,
            'Price': stock_price
        })

    # Convert to DataFrame and save to CSV
    df = pd.DataFrame(stock_data)
    df.to_csv("stock_prices.csv", index=False)
    print("Stock data saved to stock_prices.csv")
    return df

# Scrape data and save to CSV
scrape_stock_data()

# Close the WebDriver
driver.quit()
