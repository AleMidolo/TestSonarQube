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
    
    # Check if we have enough cash
    if self.cash < total_cost:
        return False
    
    # Deduct the cost from cash
    self.cash -= total_cost
    
    # Check if stock already exists in portfolio
    for existing_stock in self.portfolio:
        if existing_stock["name"] == stock["name"]:
            # Update existing stock quantity and average price
            existing_stock["quantity"] += stock["quantity"]
            return True
    
    # Add new stock to portfolio
    self.portfolio.append(stock.copy())
    return True