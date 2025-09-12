# Trading-Dashboard
# 📈 Stock Trading Assistant (Python + Streamlit)

A stock trading dashboard built with **Python, Pandas, and Streamlit** that allows users to analyze stock prices, calculate technical indicators, generate buy/sell signals, and backtest trading strategies.  

This project starts as a **minor project** but is designed to be scaled into a **major AI-powered trading system**.

---

## 🚀 Features
- 📊 Fetch historical stock data using **yfinance**  
- 📉 Technical Indicators:
  - Simple Moving Average (SMA)
  - Relative Strength Index (RSI)
  - Moving Average Convergence Divergence (MACD)  
- 💡 Buy / Sell / Hold Signal Generation  
- 🔙 Backtesting to evaluate strategy performance  
- 🌐 Interactive Dashboard using **Streamlit**  
- 💱 Currency conversion support (USD → INR)  

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Libraries:**
  - `pandas` → data handling
  - `numpy` → numerical operations
  - `matplotlib / plotly` → visualization
  - `yfinance` → stock market data
  - `streamlit` → dashboard
- **AI/ML Concepts:**
  - Rule-based expert system for Buy/Sell signals
  - Time-series analysis for stock prices  

---

## 📂 Project Structure

StockTradingAssistant/
│── dashboard/
│ └── dashboard.py # Streamlit dashboard
│── analysis/
│ └── stock_analysis.py # Core logic for indicators & backtesting
│── data/ # (Optional) Saved stock data
│── tests/
│ └── test_cases.py # Unit tests for validation
│── README.md # Documentation
