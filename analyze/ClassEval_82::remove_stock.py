def remove_stock(self, stock):
    """
        Rimuovi un'azione dal portafoglio.
        :param stock: un dizionario con le chiavi "name", "price" e "quantity"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []

        """
    for i, pf in enumerate(self.portfolio):
        if pf['name'] == stock['name']:
            if pf['quantity'] < stock['quantity']:
                return False
            elif pf['quantity'] == stock['quantity']:
                self.portfolio.pop(i)
                return True
            else:
                pf['quantity'] -= stock['quantity']
                return True
    return False