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
    name = stock['name']
    price = stock['price']
    quantity = stock['quantity']
    
    # 在投资组合中查找该股票
    for portfolio_stock in self.portfolio:
        if portfolio_stock['name'] == name:
            # 检查是否有足够的股票数量
            if portfolio_stock['quantity'] < quantity:
                return False
            
            # 卖出股票
            portfolio_stock['quantity'] -= quantity
            self.cash_balance += price * quantity
            
            # 如果股票数量为0，从投资组合中移除
            if portfolio_stock['quantity'] == 0:
                self.portfolio.remove(portfolio_stock)
            
            return True
    
    # 如果投资组合中没有该股票
    return False