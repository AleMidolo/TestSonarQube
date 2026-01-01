def get_stock_value(self, stock):
    """
        Ottieni il valore di un'azione.
        :param stock: un dizionario con le chiavi "name", "price" e "quantity"
        :return: il valore dell'azione, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        1500.0

        """
    return stock['price'] * stock['quantity']