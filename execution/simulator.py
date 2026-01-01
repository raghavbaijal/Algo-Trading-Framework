BROKERAGE = 0.001
SLIPPAGE = 0.0005

def execute_trade(signal, price, portfolio, sl_pct=0.02, tp_pct=0.04):
    # EXIT on stop-loss or take-profit
    if portfolio.position > 0:
        if price <= portfolio.stop_loss or price >= portfolio.take_profit:
            effective_price = price * (1 - SLIPPAGE)
            trade_value = portfolio.position * effective_price
            cost = trade_value * BROKERAGE

            portfolio.capital += (trade_value - cost)
            portfolio.reset_position()
            return

    # BUY
    if signal == 1 and portfolio.position == 0:
        effective_price = price * (1 + SLIPPAGE)
        quantity = portfolio.capital // effective_price
        if quantity == 0:
            return

        trade_value = quantity * effective_price
        cost = trade_value * BROKERAGE

        portfolio.capital -= (trade_value + cost)
        portfolio.position = quantity
        portfolio.set_risk_levels(effective_price, sl_pct, tp_pct)

    # SELL
    if signal == -1 and portfolio.position > 0:
        effective_price = price * (1 - SLIPPAGE)
        trade_value = portfolio.position * effective_price
        cost = trade_value * BROKERAGE

        portfolio.capital += (trade_value - cost)
        portfolio.reset_position()
