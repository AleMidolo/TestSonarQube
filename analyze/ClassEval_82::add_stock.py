def add_stock(self, stock):
    """
        Agrega una acción al portafolio.
        :param stock: un diccionario con las claves "name", "price" y "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        """
    for pf in self.portfolio:
        if pf['name'] == stock['name']:
            pf['quantity'] += stock['quantity']
            return
    self.portfolio.append(stock.copy())