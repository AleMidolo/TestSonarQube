def get_portfolio_summary(self):
    """
    पोर्टफोलियो का सारांश प्राप्त करें।
    :return: पोर्टफोलियो का कुल मूल्य और "name" और "value" कुंजी वाले शब्दकोशों की सूची का एक ट्यूपल
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