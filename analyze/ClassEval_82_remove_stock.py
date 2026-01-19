def remove_stock(self, stock):
    """
    Remove a stock from the portfolio.
    :param stock: a dictionary with keys "name", "price", and "quantity"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    True
    >>> tracker.portfolio
    []

    """
    for i, portfolio_stock in enumerate(self.portfolio):
        if portfolio_stock['name'] == stock['name']:
            self.portfolio.pop(i)
            return True
    return False