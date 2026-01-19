def remove_stock(self, stock):
    """
    从投资组合中移除一只股票。
    :param stock: 一个包含键 "name"、"price" 和 "quantity" 的字典
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
    >>> tracker.remove_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    True
    >>> tracker.portfolio
    []

    """
    for i, portfolio_stock in enumerate(self.portfolio):
        if portfolio_stock['name'] == stock['name']:
            if portfolio_stock['quantity'] == stock['quantity']:
                self.portfolio.pop(i)
                return True
            elif portfolio_stock['quantity'] > stock['quantity']:
                portfolio_stock['quantity'] -= stock['quantity']
                return True
            else:
                return False
    return False