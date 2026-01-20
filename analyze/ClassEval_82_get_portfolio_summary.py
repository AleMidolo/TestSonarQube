def get_portfolio_summary(self):
    """
    Obtiene un resumen del portafolio.
    :return: una tupla del valor total del portafolio y una lista de diccionarios con las claves "name" y "value"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.get_portfolio_summary()
    (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

    """
    portfolio_list = []
    total_portfolio_value = self.cash
    
    for stock in self.portfolio:
        stock_value = stock['price'] * stock['quantity']
        portfolio_list.append({'name': stock['name'], 'value': stock_value})
        total_portfolio_value += stock_value
    
    return (total_portfolio_value, portfolio_list)