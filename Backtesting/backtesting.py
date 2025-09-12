
"""
Backtesting Module

This module implements a simple backtesting engine to evaluate
trading strategy performance by simulating trades based on signals.
"""


def backtest(df, initial_capital=10000):
    """
    Simulate trading based on buy/sell signals and calculate profit/loss.
    
    Trading Logic:
    - Buy signal: Use all available capital to buy shares
    - Sell signal: Sell all shares and convert back to cash
    - Hold signal: No action taken
    
    Args:
        df (pandas.DataFrame): DataFrame with columns ['Signal', 'Close']
        initial_capital (float): Starting capital amount (default: $10,000)
        
    Returns:
        float: Net profit/loss from the trading strategy
    """
    # Initialize tracking variables
    capital = initial_capital  # Available cash
    position = 0  # Number of shares held
    
    # Simulate trading for each day
    for i in range(len(df)):
        signal = df['Signal'].iloc[i]
        price = df['Close'].iloc[i]
        
        # Execute buy signal: convert all cash to shares
        if signal == "Buy" and capital > 0:
            position = capital / price  # Calculate shares to buy
            capital = 0  # All cash converted to shares
            
        # Execute sell signal: convert all shares to cash
        elif signal == "Sell" and position > 0:
            capital = position * price  # Calculate cash from selling shares
            position = 0  # All shares sold
    
    # Calculate final portfolio value
    final_value = capital + (position * df['Close'].iloc[-1]) if position > 0 else capital
    
    # Return net profit/loss
    return final_value - initial_capital
