def get_portfolio_summary(self):
    """
        Get a summary of the portfolio.
        :return: a tuple of the total value of the portfolio and a list of dictionaries with keys "name" and "value"
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])
        """
    total_value = self.calculate_portfolio_value()
    summary = [{'name': stock['name'], 'value': self.get_stock_value(stock)} for stock in self.portfolio]
    return (total_value, summary)