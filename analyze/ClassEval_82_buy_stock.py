def buy_stock(self, stock):
    """
        Compra una acción y añádela al portafolio.
        :param stock: un diccionario con las claves "name", "price" y "quantity"
        :param quantity: la cantidad de la acción a comprar, int.
        :return: True si la acción fue comprada con éxito, False si el saldo en efectivo no es suficiente.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

        """
    cost = stock['price'] * stock['quantity']
    if cost > self.cash_balance:
        return False
    self.cash_balance -= cost
    for pf in self.portfolio:
        if pf['name'] == stock['name']:
            pf['quantity'] += stock['quantity']
            return True
    self.portfolio.append(stock)
    return True