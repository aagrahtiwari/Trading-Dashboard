"""
Trading Dashboard

Interactive Streamlit web application for stock analysis and trading strategy backtesting.
This dashboard allows users to:
- Enter stock tickers
- Fetch real-time data
- Calculate technical indicators
- Generate trading signals
- Run backtesting simulations
- Visualize results with charts
"""

import streamlit as st
import pandas as pd
import sys
import os

# Add parent directory to Python path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import our custom modules
from Utils.data_fetcher import fetch_stock_data
from Indicators.technicals import SMA, RSI
from Strategies.simple_strategy import generate_signals
from Backtesting.backtesting import backtest

# Configure Streamlit page
st.set_page_config(
    page_title="Stock Trading Assistant",
    page_icon="📈",
    layout="wide"
)

# Main dashboard interface
st.title("📈 Stock Trading Assistant")
st.markdown("**Analyze stocks and test trading strategies with real-time data**")

# Sidebar for user inputs
st.sidebar.header("📊 Analysis Parameters")
ticker = st.sidebar.text_input("Stock Ticker:", "AAPL", help="Enter a valid stock symbol (e.g., AAPL, MSFT, GOOGL)")
start_date = st.sidebar.date_input("Start Date:", value=pd.Timestamp("2023-01-01"))
end_date = st.sidebar.date_input("End Date:", value=pd.Timestamp("2024-01-01"))

# Main analysis button
if st.button("🚀 Run Analysis", type="primary"):
    try:
        with st.spinner("Fetching data and running analysis..."):
            # Step 1: Fetch stock data
            st.info("📥 Fetching stock data...")
            df = fetch_stock_data(ticker, str(start_date), str(end_date))
            
            if df.empty:
                st.error("❌ No data found for this ticker. Please try a different symbol.")
            else:
                # Step 2: Calculate technical indicators
                st.info("📊 Calculating technical indicators...")
                df = SMA(df, 50)   # 50-day Simple Moving Average
                df = SMA(df, 200)  # 200-day Simple Moving Average
                df = RSI(df, 14)   # 14-day Relative Strength Index
                
                # Step 3: Generate trading signals
                st.info("🎯 Generating trading signals...")
                df = generate_signals(df)
                
                # Step 4: Run backtesting
                st.info("💰 Running backtesting simulation...")
                profit = backtest(df)
                
                # Display results
                st.success("✅ Analysis completed successfully!")
                
                # Main metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Strategy Profit", f"${profit:.2f}", 
                             delta=f"{profit/10000*100:.1f}%" if profit != 0 else "0%")
                with col2:
                    st.metric("Total Trades", len(df[df['Signal'] != 'Hold']))
                with col3:
                    st.metric("Buy Signals", len(df[df['Signal'] == 'Buy']))
                with col4:
                    st.metric("Sell Signals", len(df[df['Signal'] == 'Sell']))
                
                # Price and indicators chart
                st.subheader("📈 Price Chart with Technical Indicators")
                chart_data = df[['Date', 'Close', 'SMA_50', 'SMA_200']].set_index('Date')
                st.line_chart(chart_data)
                
                # Trading signals visualization
                st.subheader("🎯 Trading Signals")
                signal_counts = df['Signal'].value_counts()
                st.bar_chart(signal_counts)
                
                # Data summary
                with st.expander("📋 View Raw Data"):
                    st.dataframe(df.tail(10))
                    
    except Exception as e:
        st.error(f"❌ Error running analysis: {str(e)}")
        st.write("Please check the ticker symbol and try again.")
        st.write("**Common issues:**")
        st.write("- Invalid ticker symbol")
        st.write("- Network connection problems")
        st.write("- Date range issues")

# Footer
st.markdown("---")
st.markdown("**Built with Streamlit** | *For educational purposes only*")
