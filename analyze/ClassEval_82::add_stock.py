def add_stock(self, stock):
    """
        Aggiungi un'azione al portafoglio.
        :param stock: un dizionario con le chiavi "name", "price" e "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.add_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        """
    for pf in self.portfolio:
        if pf['name'] == stock['name']:
            pf['quantity'] += stock['quantity']
            return
    self.portfolio.append(stock)