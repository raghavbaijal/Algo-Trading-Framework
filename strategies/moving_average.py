from strategies.base import Strategy

class MovingAverageStrategy(Strategy):
    def __init__(self, short_window=10, long_window=30):
        self.short_window = short_window
        self.long_window = long_window

def generate_signals(data):
    data["short_ma"] = data["close"].rolling(20).mean()
    data["long_ma"] = data["close"].rolling(50).mean()
    data["signal"] = (data["short_ma"] > data["long_ma"]).astype(int)
    return data

