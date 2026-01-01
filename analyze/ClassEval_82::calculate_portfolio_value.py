def calculate_portfolio_value(self):
    """
    पोर्टफोलियो की कुल वैल्यू कैलकुलेट करें।

    :return: float, पोर्टफोलियो की कुल वैल्यू

    >>> ट्रैकर = StockPortfolioTracker(10000.0)
    >>> ट्रैकर.पोर्टफोलियो = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> ट्रैकर.calculate_portfolio_value()
    11500.0
    """
    total_value = self.cash_balance
    for stock in self.portfolio:
        total_value += self.get_stock_value(stock)
    return total_value