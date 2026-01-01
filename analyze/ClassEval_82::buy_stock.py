def buy_stock(self, stock):
    """
        购买股票并将其添加到投资组合中。
        :param stock: 一个字典，包含键 "name"、"price" 和 "quantity"
        :param quantity: 要购买的股票数量，int。
        :return: 如果股票成功购买则返回 True，如果现金余额不足则返回 False。
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
        True
        >>> tracker.portfolio
        [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

        """
    cost = stock['price'] * stock['quantity']
    if cost > self.cash_balance:
        return False
    self.cash_balance -= cost
    self.add_stock(stock)
    return True