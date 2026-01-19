def get_portfolio_summary(self):
    """
    Get a summary of the portfolio.
    :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.get_portfolio_summary()
    (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

    """
    summary_list = []
    total_portfolio_value = 0.0
    
    for stock in self.portfolio:
        stock_value = stock['price'] * stock['quantity']
        summary_list.append({'name': stock['name'], 'value': stock_value})
        total_portfolio_value += stock_value
    
    # Add cash to total value
    total_portfolio_value += self.cash
    
    return (total_portfolio_value, summary_list)