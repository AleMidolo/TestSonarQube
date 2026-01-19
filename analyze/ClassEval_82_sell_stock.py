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
    for i, portfolio_stock in enumerate(self.portfolio):
        if portfolio_stock['name'] == name:
            # Verifica se la quantità è sufficiente
            if portfolio_stock['quantity'] < quantity:
                return False
            
            # Aggiungi il denaro al saldo di cassa
            self.cash_balance += price * quantity
            
            # Riduci la quantità o rimuovi l'azione dal portafoglio
            if portfolio_stock['quantity'] == quantity:
                # Rimuovi completamente l'azione
                self.portfolio.pop(i)
            else:
                # Riduci la quantità
                portfolio_stock['quantity'] -= quantity
            
            return True
    
    # Se l'azione non è stata trovata nel portafoglio
    return False