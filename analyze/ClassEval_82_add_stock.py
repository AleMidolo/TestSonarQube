def add_stock(self, stock):
    """
    将股票添加到投资组合中。
    :param stock: 一个字典，包含键 "name"、"price" 和 "quantity"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    >>> tracker.portfolio
    [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

    """
    self.portfolio.append(stock)