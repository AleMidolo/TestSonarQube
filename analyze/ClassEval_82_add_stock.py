def add_stock(self, stock):
    """
    Add a stock to the portfolio.
    :param stock: a dictionary with keys "name", "price", and "quantity"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    >>> tracker.portfolio
    [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

    """
    self.portfolio.append(stock)