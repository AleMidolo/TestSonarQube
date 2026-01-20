def get_portfolio_summary(self):
    """
    Obtiene un resumen del portafolio.
    :return: una tupla del valor total del portafolio y una lista de diccionarios con las claves "name" y "value"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.get_portfolio_summary()
    (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

    """
    portfolio_value = sum(stock['price'] * stock['quantity'] for stock in self.portfolio)
    total_value = self.cash + portfolio_value
    
    summary_list = [
        {'name': stock['name'], 'value': stock['price'] * stock['quantity']}
        for stock in self.portfolio
    ]
    
    return (total_value, summary_list)