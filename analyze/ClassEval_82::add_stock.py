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
            if existing_stock['price'] == stock['price']:
                existing_stock['quantity'] += stock['quantity']
            else:
                self.portfolio.append(stock.copy())
            return
    self.portfolio.append(stock.copy())