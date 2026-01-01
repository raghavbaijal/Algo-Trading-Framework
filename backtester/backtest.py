from execution.simulator import execute_trade
from portfolio.portfolio import Portfolio

def run_backtest(data, strategy, initial_capital=100000):
    data = strategy(data)   # 👈 apply strategy here

    cash = initial_capital
    position = 0
    history = []

    for i in range(1, len(data)):
        price = data["close"].iloc[i]
        signal = data["signal"].iloc[i]
        date = data.index[i]

        if signal == 1 and position == 0:
            position = cash / price
            cash = 0

        elif signal == 0 and position > 0:
            cash = position * price
            position = 0

        portfolio_value = cash + position * price
        history.append((date, portfolio_value))

    return type("Portfolio", (), {"history": history})
