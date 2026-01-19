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
    total_cost = stock["price"] * stock["quantity"]
    
    if self.cash_balance >= total_cost:
        self.cash_balance -= total_cost
        
        # 检查投资组合中是否已存在该股票
        existing_stock = None
        for s in self.portfolio:
            if s["name"] == stock["name"]:
                existing_stock = s
                break
        
        if existing_stock:
            # 更新现有股票的数量和平均价格
            total_quantity = existing_stock["quantity"] + stock["quantity"]
            total_value = existing_stock["price"] * existing_stock["quantity"] + total_cost
            existing_stock["price"] = total_value / total_quantity
            existing_stock["quantity"] = total_quantity
        else:
            # 添加新股票到投资组合
            self.portfolio.append(stock.copy())
        
        return True
    else:
        return False