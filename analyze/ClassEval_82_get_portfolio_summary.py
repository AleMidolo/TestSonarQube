def get_portfolio_summary(self):
    """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """
    stock_values = []
    for stock in self.portfolio:
        stock_values.append({'name': stock['name'], 'value': stock['price'] * stock['quantity']})
    total_value = self.calculate_portfolio_value()
    return (total_value, stock_values)