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
    name = stock['name']
    price = stock['price']
    quantity = stock['quantity']
    
    # Cerca l'azione nel portafoglio
    for item in self.portfolio:
        if item['name'] == name:
            # Verifica se la quantità è sufficiente
            if item['quantity'] < quantity:
                return False
            
            # Aggiungi il denaro al saldo di cassa
            self.cash_balance += price * quantity
            
            # Riduci la quantità dell'azione
            item['quantity'] -= quantity
            
            # Se la quantità diventa 0, rimuovi l'azione dal portafoglio
            if item['quantity'] == 0:
                self.portfolio.remove(item)
            
            return True
    
    # Se l'azione non è stata trovata nel portafoglio
    return False