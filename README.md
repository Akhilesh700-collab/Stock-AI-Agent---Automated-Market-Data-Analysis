# AI Stock Analysis Agent

This project implements a Python-based AI agent that automatically fetches
stock market data, analyzes key financial metrics, applies heuristic-based
and RSI-driven predictions, and generates automated reports.

## Features
- Real-time stock data using Yahoo Finance
- Technical indicators (SMA, RSI)
- Heuristic-based trend prediction
- Modular architecture
- Automated reporting

## Project Structure
```stock-ai-agent/
├── main.py              # Main controller to run the agent
├── data_fetcher.py      # Fetches stock market data from public APIs
├── analytics.py         # Calculates metrics like SMA and RSI
├── agent.py             # Applies heuristic-based prediction logic
├── report.py            # Dumps summary report to console
├── requirements.txt     # Project dependencies
├── DESIGN_DOCUMENT.md   # Design and rationale documentation
└── README.md            # Project overview and usage instructions```
