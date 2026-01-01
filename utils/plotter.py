import matplotlib.pyplot as plt

def plot_equity_curve(equity):
    plt.figure(figsize=(10, 5))
    plt.plot(equity)
    plt.title("Equity Curve")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.show()
