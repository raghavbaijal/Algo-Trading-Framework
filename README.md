# Algorithmic Trading Framework (Python)

A single-asset algorithmic trading backtesting and paper-trading system built in Python with realistic execution modeling and risk management.

## Features
- Real historical OHLCV data (Yahoo Finance)
- Rule-based trading strategy
- Realistic execution with slippage & transaction costs
- Stop-loss and take-profit risk management
- Candle-by-candle backtesting (no lookahead bias)
- Performance evaluation (Sharpe ratio, max drawdown)
- Equity curve visualization

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib
- yfinance

## How It Works
1. Load historical market data
2. Generate trading signals
3. Execute trades with slippage & brokerage
4. Enforce risk management rules
5. Track portfolio equity and performance metrics

## How to Run
```bash
pip install -r requirements.txt
python main.py
