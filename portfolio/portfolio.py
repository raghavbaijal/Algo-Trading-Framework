import pandas as pd

class Portfolio:
    def __init__(self, capital):
        self.capital = capital
        self.position = 0
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None
        self.history = []

    def update(self, date, price):
        equity = self.capital + self.position * price
        self.history.append({"date": date, "equity": equity})

    def set_risk_levels(self, entry_price, sl_pct, tp_pct):
        self.entry_price = entry_price
        self.stop_loss = entry_price * (1 - sl_pct)
        self.take_profit = entry_price * (1 + tp_pct)

    def reset_position(self):
        self.position = 0
        self.entry_price = None
        self.stop_loss = None
        self.take_profit = None

    def equity_curve(self):
        df = pd.DataFrame(self.history)
        df.set_index("date", inplace=True)
        return df
