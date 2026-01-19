def get_portfolio_summary(self):
    """
    获取投资组合的摘要。
    :return: 投资组合的总价值和一个包含键 "name" 和 "value" 的字典列表的元组
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.get_portfolio_summary()
    (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

    """
    portfolio_value = 0.0
    summary_list = []
    
    for stock in self.portfolio:
        stock_value = stock['price'] * stock['quantity']
        portfolio_value += stock_value
        summary_list.append({'name': stock['name'], 'value': stock_value})
    
    total_value = self.cash + portfolio_value
    
    return (total_value, summary_list)