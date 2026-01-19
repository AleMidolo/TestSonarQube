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
    total_cost = stock["price"] * stock["quantity"]
    
    if self.cash >= total_cost:
        self.cash -= total_cost
        self.portfolio.append(stock)
        return True
    else:
        return False