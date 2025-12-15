def calculate_portfolio_value(self):
    """
    Calculate the total value of the portfolio.

    :return: float, total value of the portfolio

    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.calculate_portfolio_value()
    1500.0
    """
    total_value = 0.0
    for stock in self.portfolio:
        total_value += self.get_stock_value(stock)
    return total_value + self.cash_balance