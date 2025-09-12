

"""
Technical Indicators Module

This module contains functions to calculate various technical indicators
used in trading analysis, such as Simple Moving Averages and RSI.
"""


def SMA(df, period=50):
    """
    Calculate Simple Moving Average (SMA) for a given period.
    
    SMA is the average price over a specified number of periods.
    It helps smooth out price fluctuations and identify trends.
    
    Args:
        df (pandas.DataFrame): DataFrame with 'Close' column
        period (int): Number of periods for the moving average (default: 50)
        
    Returns:
        pandas.DataFrame: DataFrame with added SMA column
    """
    # Calculate rolling mean of closing prices
    df[f"SMA_{period}"] = df['Close'].rolling(window=period).mean()
    return df


def RSI(df, period=14):
    """
    Calculate Relative Strength Index (RSI) for a given period.
    
    RSI is a momentum oscillator that measures the speed and magnitude
    of price changes. Values range from 0 to 100:
    - RSI > 70: Overbought (potential sell signal)
    - RSI < 30: Oversold (potential buy signal)
    
    Args:
        df (pandas.DataFrame): DataFrame with 'Close' column
        period (int): Number of periods for RSI calculation (default: 14)
        
    Returns:
        pandas.DataFrame: DataFrame with added RSI column
    """
    # Calculate price changes (deltas)
    delta = df['Close'].diff()
    
    # Separate gains and losses
    gain = delta.where(delta > 0, 0).rolling(period).mean()  # Average gains
    loss = -delta.where(delta < 0, 0).rolling(period).mean()  # Average losses
    
    # Calculate Relative Strength (RS)
    rs = gain / loss
    
    # Calculate RSI using the standard formula
    df['RSI'] = 100 - (100 / (1 + rs))
    
    return df
