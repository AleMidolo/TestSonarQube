def get_stock_value(self, stock):
    """
        Obtiene el valor de una acción.
        :param stock: un diccionario con las claves "name", "price" y "quantity"
        :return: el valor de la acción, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        1500.0
        """
    return stock['price'] * stock['quantity']