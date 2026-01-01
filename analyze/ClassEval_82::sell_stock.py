def sell_stock(self, stock):
    """
        Vender una acción y eliminarla del portafolio y agregar el efectivo al saldo de efectivo.
        :param stock: un diccionario con las claves "name", "price" y "quantity"
        :param quantity: la cantidad de la acción a vender, int.
        :return: True si la acción se vendió con éxito, False si la cantidad de la acción no es suficiente.
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