def add_stock(self, stock):
    """
        Aggiungi un'azione al portafoglio.
        :param stock: un dizionario con le chiavi "name", "price" e "quantity"
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