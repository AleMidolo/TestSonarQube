def get_portfolio_summary(self):
    """
    Ottieni un riepilogo del portafoglio.
    :return: una tupla del valore totale del portafoglio e una lista di dizionari con le chiavi "name" e "value"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.get_portfolio_summary()
    (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

    """
    portfolio_items = []
    total_portfolio_value = self.cash
    
    for stock in self.portfolio:
        stock_value = stock['price'] * stock['quantity']
        portfolio_items.append({
            'name': stock['name'],
            'value': stock_value
        })
        total_portfolio_value += stock_value
    
    return (total_portfolio_value, portfolio_items)