def add_stock(self, stock):
    """
        Add a stock to the portfolio.
        :param stock: a dictionary with keys "name", "price", and "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        """
    for existing_stock in self.portfolio:
        if existing_stock['name'] == stock['name']:
            existing_stock['quantity'] += stock['quantity']
            return
    self.portfolio.append(stock.copy())