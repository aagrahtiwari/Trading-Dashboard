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


---

## ⚙️ Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/StockTradingAssistant.git
   cd Trading-Dashboard
   
2. **Install Dependencies**
  pip install -r requirements.txt

3. **Run the Dashboard**
  python -m streamlit run dashboard/dashboard.py

4. **Access the App**
  Open browser → http://localhost:8501


## ✅ Test Cases

*Input*: Stock ticker AAPL, SMA(20), SMA(50)
*Output*: Buy signal generated when SMA(20) > SMA(50).

*Input*: Stock ticker TSLA, RSI(14)
*Output*: RSI > 70 → Overbought (Sell signal), RSI < 30 → Oversold (Buy signal).

*Input*: Backtest period 2022-01-01 to 2023-01-01
*Output*: Strategy return % vs Benchmark return %.

