def add_stock(self, stock):
    """
        将股票添加到投资组合中。
        :param stock: 一个字典，包含键 "name"、"price" 和 "quantity"
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