def calculate_portfolio_value(self):
    """
        Calcular el valor total del portafolio.
        :return: el valor total del portafolio, float.
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.calculate_portfolio_value()
        11500.0

        """
    total_value = self.cash_balance
    for stock in self.portfolio:
        total_value += self.get_stock_value(stock)
    return total_value