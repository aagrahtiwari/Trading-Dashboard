
"""
Simple Trading Strategy Module

This module implements a basic trading strategy based on:
- Simple Moving Averages (SMA) crossover
- Relative Strength Index (RSI) overbought/oversold conditions
"""


def generate_signals(df):
    """
    Generate buy/sell signals based on technical indicators.
    
    Strategy Logic:
    - Buy: SMA_50 > SMA_200 AND RSI < 70 (uptrend + not overbought)
    - Sell: SMA_50 < SMA_200 OR RSI > 70 (downtrend or overbought)
    - Hold: All other conditions
    
    Args:
        df (pandas.DataFrame): DataFrame with columns ['SMA_50', 'SMA_200', 'RSI']
        
    Returns:
        pandas.DataFrame: DataFrame with added 'Signal' column
    """
    # Create a copy to avoid modifying the original DataFrame
    df = df.copy()
    
    # Initialize all signals as 'Hold'
    df['Signal'] = "Hold"
    
    # Generate signals for each row (skip first row as we need previous data)
    for i in range(1, len(df)):
        # Get current values using .iloc for position-based indexing
        sma_50 = df['SMA_50'].iloc[i]
        sma_200 = df['SMA_200'].iloc[i]
        rsi = df['RSI'].iloc[i]
        
        # Buy signal: Golden cross (SMA_50 > SMA_200) and RSI not overbought
        if sma_50 > sma_200 and rsi < 70:
            df.loc[i, 'Signal'] = "Buy"
            
        # Sell signal: Death cross (SMA_50 < SMA_200) or RSI overbought
        elif sma_50 < sma_200 or rsi > 70:
            df.loc[i, 'Signal'] = "Sell"
    
    return df
