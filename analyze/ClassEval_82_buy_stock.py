def buy_stock(self, stock):
    """
    Acquista un'azione e aggiungila al portafoglio.
    :param stock: un dizionario con le chiavi "name", "price" e "quantity"
    :param quantity: la quantità dell'azione da acquistare, int.
    :return: True se l'azione è stata acquistata con successo, False se il saldo disponibile non è sufficiente.
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    True
    >>> tracker.portfolio
    [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

    """
    total_cost = stock["price"] * stock["quantity"]
    
    if self.balance >= total_cost:
        self.balance -= total_cost
        self.portfolio.append(stock)
        return True
    else:
        return False