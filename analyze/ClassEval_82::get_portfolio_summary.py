def get_portfolio_summary(self):
    """
        获取投资组合的摘要。
        :return: 投资组合的总价值和一个包含键 "name" 和 "value" 的字典列表的元组
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.get_portfolio_summary()
        (11500.0, [{'name': 'AAPL', 'value': 1500.0}])
        """
    total_value = self.calculate_portfolio_value()
    summary = [{'name': stock['name'], 'value': self.get_stock_value(stock)} for stock in self.portfolio]
    return (total_value, summary)