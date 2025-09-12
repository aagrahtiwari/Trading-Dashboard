"""
Main Entry Point for Trading Dashboard

This script serves as the main entry point for the trading dashboard application.
It launches the Streamlit web interface for stock analysis and backtesting.
"""

import subprocess
import sys

if __name__ == "__main__":
    """
    Launch the Streamlit trading dashboard.
    
    This will start a local web server and open the dashboard in your browser.
    The dashboard will be accessible at http://localhost:8501
    """
    print("🚀 Starting Trading Dashboard...")
    print("📊 Dashboard will be available at: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the server")
    
    # Run the Streamlit dashboard
    subprocess.run([
        sys.executable, "-m", "streamlit", "run", "Dashboard/dashboard.py"
    ])
