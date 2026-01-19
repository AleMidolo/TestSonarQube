def get_portfolio_summary(self):
    """
    पोर्टफोलियो का सारांश प्राप्त करें।
    :return: पोर्टफोलियो का कुल मूल्य और "name" और "value" कुंजी वाले शब्दकोशों की सूची का एक ट्यूपल
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.get_portfolio_summary()
    (11500.0, [{'name': 'AAPL', 'value': 1500.0}])

    """
    # Calculate the total value of all stocks in the portfolio
    stocks_value = sum(stock['price'] * stock['quantity'] for stock in self.portfolio)
    
    # Calculate total portfolio value (cash + stocks)
    total_value = self.cash + stocks_value
    
    # Create summary list with name and value for each stock
    summary_list = [
        {
            'name': stock['name'],
            'value': stock['price'] * stock['quantity']
        }
        for stock in self.portfolio
    ]
    
    return (total_value, summary_list)