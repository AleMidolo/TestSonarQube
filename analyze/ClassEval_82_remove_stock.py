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
    for pf in self.portfolio:
        if pf['name'] == stock['name']:
            if pf['quantity'] < stock['quantity']:
                return False
            pf['quantity'] -= stock['quantity']
            if pf['quantity'] == 0:
                self.portfolio.remove(pf)
            return True
    return False