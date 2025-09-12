"""
Data Fetcher Module

This module handles fetching stock data from Yahoo Finance
and saving it to local CSV files for analysis.
"""

import yfinance as yf
import pandas as pd
import os


def fetch_stock_data(ticker, start, end):
    """
    Fetch stock data from Yahoo Finance and save to CSV.
    
    Args:
        ticker (str): Stock symbol (e.g., 'AAPL', 'MSFT')
        start (str): Start date in 'YYYY-MM-DD' format
        end (str): End date in 'YYYY-MM-DD' format
        
    Returns:
        pandas.DataFrame: Stock data with columns ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
    """
    # Download stock data from Yahoo Finance
    df = yf.download(ticker, start=start, end=end)
    
    # Flatten MultiIndex columns if they exist (yfinance sometimes returns MultiIndex)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel(1)
    
    # Reset index to make Date a regular column instead of index
    df = df.reset_index()
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join("Data", "raw")
    os.makedirs(output_dir, exist_ok=True)
    
    # Save data to CSV file
    output_path = os.path.join(output_dir, f"{ticker}.csv")
    df.to_csv(output_path, index=False)
    
    return df
