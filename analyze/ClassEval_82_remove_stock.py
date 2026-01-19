def remove_stock(self, stock):
    """
    Eliminar una acción del portafolio.
    :param stock: un diccionario con las claves "name", "price" y "quantity"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    True
    >>> tracker.portfolio
    []

    """
    for i, item in enumerate(self.portfolio):
        if item['name'] == stock['name']:
            self.portfolio.pop(i)
            return True
    return False