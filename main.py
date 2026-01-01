from data.price_data import load_data
from strategies.moving_average import generate_signals
from backtester.backtest import run_backtest
from utils.plotter import plot_equity_curve

# Load data
data = load_data(
    symbol="^NSEI",
    start="2018-01-01",
    end="2025-01-01"
)

# Run backtest by passing strategy
portfolio = run_backtest(
    data,
    strategy=generate_signals
)

# Results
final_date, final_value = portfolio.history[-1]
print(f"Final Portfolio Value on {final_date.date()}: ₹{final_value:,.2f}")

# Plot equity curve
equity_curve = [v for _, v in portfolio.history]
plot_equity_curve(equity_curve)
