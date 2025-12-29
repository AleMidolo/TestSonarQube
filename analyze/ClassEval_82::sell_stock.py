def sell_stock(self, stock):
    """
        Vendi un'azione e rimuovila dal portafoglio e aggiungi il denaro al saldo di cassa.
        :param stock: un dizionario con le chiavi "name", "price" e "quantity"
        :param quantity: la quantità dell'azione da vendere, int.
        :return: True se l'azione è stata venduta con successo, False se la quantità dell'azione non è sufficiente.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []

        """
    for pf in self.portfolio:
        if pf['name'] == stock['name'] and pf['quantity'] >= stock['quantity']:
            pf['quantity'] -= stock['quantity']
            self.cash_balance += stock['price'] * stock['quantity']
            if pf['quantity'] == 0:
                self.portfolio.remove(pf)
            return True
    return False