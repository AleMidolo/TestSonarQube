def get_portfolio_summary(self):
    """
        Ottieni un riepilogo del portafoglio.
        :return: una tupla del valore totale del portafoglio e una lista di dizionari con le chiavi "name" e "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """
    stock_values = []
    for stock in self.portfolio:
        stock_value = {'name': stock['name'], 'value': stock['price'] * stock['quantity']}
        stock_values.append(stock_value)
    total_value = self.calculate_portfolio_value()
    return (total_value, stock_values)