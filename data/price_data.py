import yfinance as yf

def load_data(symbol, start, end, interval="1d"):
    data = yf.download(
        symbol,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=True,
        progress=False
    )

    data.dropna(inplace=True)

    # 🔥 FIX: flatten MultiIndex columns safely
    if isinstance(data.columns, type(data.columns)) and hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    data.columns = [str(c).lower() for c in data.columns]

    return data
