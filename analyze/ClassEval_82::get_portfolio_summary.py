def get_portfolio_summary(self):
    """
        पोर्टफोलियो का सारांश प्राप्त करें।
        :return: पोर्टफोलियो का कुल मूल्य और "name" और "value" कुंजी वाले शब्दकोशों की सूची का एक ट्यूपल
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

        """
    total_value = self.calculate_portfolio_value()
    stock_summary = []
    for stock in self.portfolio:
        stock_value = stock['price'] * stock['quantity']
        stock_summary.append({'name': stock['name'], 'value': stock_value})
    return (total_value, stock_summary)