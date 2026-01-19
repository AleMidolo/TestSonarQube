def calculate_portfolio_value(self):
    """
    Calcola il valore totale del portafoglio.
    :return: il valore totale del portafoglio, float.
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.calculate_portfolio_value()
    11500.0

    """
    portfolio_value = sum(stock['price'] * stock['quantity'] for stock in self.portfolio)
    return self.cash + portfolio_value