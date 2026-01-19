def sell_stock(self, stock):
    """
        卖出股票并将其从投资组合中移除，并将现金添加到现金余额中。
        :param stock: 一个字典，包含键 "name"、"price" 和 "quantity"
        :param quantity: 要出售的股票数量，int。
        :return: 如果股票成功出售则返回 True，如果股票数量不足则返回 False。
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.portfolio = [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]
        >>> tracker.sell_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        []
        """
    for pf in self.portfolio:
        if pf['name'] == stock['name'] and pf['quantity'] >= stock['quantity']:
            pf['quantity'] -= stock['quantity']
            self.cash_balance += stock['price'] * stock['quantity']
            if pf['quantity'] == 0:
                self.portfolio.remove(pf)
            return True
    return False