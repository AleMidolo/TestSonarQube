def add_stock(self, stock):
    """
    पोर्टफोलियो में एक स्टॉक जोड़ें।
    :param stock: एक शब्दकोश जिसमें कुंजी "name", "price", और "quantity" हैं
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    >>> tracker.portfolio
    [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

    """
    self.portfolio.append(stock)