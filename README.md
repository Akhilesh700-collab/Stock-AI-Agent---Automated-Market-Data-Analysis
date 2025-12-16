# Stock AI Agent - Automated Market Data Analysis & Trend Prediction System

This project implements a Python-based AI agent that automatically fetches stock market data, analyzes key financial metrics, applies heuristic-based and RSI-driven predictions, and generates automated reports.

##  Problem Statement

Retail investors often struggle to analyze large volumes of stock market data and identify short-term trends using technical indicators.
This project aims to automate stock data collection, indicator computation, trend analysis, and reporting using an AI-style agent pipeline.

##  Architecture Overview

1. Fetch real-time stock data using public APIs
2. Compute technical indicators (SMA, RSI)
3. Analyze price trends using rule-based logic
4. Generate structured daily stock reports
5. Display insights in a readable format

## Features
- Real-time stock data using Yahoo Finance
- Technical indicators (SMA, RSI)
- Heuristic-based trend prediction
- Modular architecture
- Automated reporting

##  Technologies Used

- Programming Language: Python
- Libraries: yfinance, pandas, numpy
- Concepts: AI Agents, Technical Analysis, Time-Series Data
- Tools: Git, GitHub, VS Code

## Project Structure
     stock-ai-agent/
├── main.py              # Main controller to run the agent
├── data_fetcher.py      # Fetches stock market data from public APIs
├── analytics.py         # Calculates metrics like SMA and RSI
├── agent.py             # Applies heuristic-based prediction logic
├── report.py            # Dumps summary report to console
├── requirements.txt     # Project dependencies
├── DESIGN_DOCUMENT.md   # Design and rationale documentation
└── README.md            # Project overview and usage instructions

##  Sample Output

==============================
DAILY STOCK REPORT
==============================
Stock: AAPL
Current Price: 189.23
Change: +2.15 (1.14%)
Volume: 52,340,000
RSI: 68.2
Trend: Bullish (Price above 5-day SMA)

##  Why This Is an AI Agent

This system behaves like an AI agent because it:
- Autonomously fetches data
- Analyzes market conditions
- Applies decision logic
- Generates actionable insights without human intervention

##  Current Limitations

- Uses rule-based logic instead of ML models
- No backtesting implemented
- No graphical dashboard
- Predictions are short-term heuristics

##  Future Enhancements

- Machine Learning models (LSTM, Random Forest)
- Backtesting and strategy evaluation
- News sentiment analysis
- Streamlit-based dashboard
- Cloud deployment.

plt.savefig("results/price_trend.png")
plt.show()
