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
                elif pf['quantity'] == stock['quantity']:
                    self.portfolio.remove(pf)
                else:
                    pf['quantity'] -= stock['quantity']
                return True
        return False