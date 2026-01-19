def buy_stock(self, stock):
    """
    Buy a stock and add it to the portfolio.
    :param stock: a dictionary with keys "name", "price", and "quantity"
    :param quantity: the quantity of the stock to buy,int.
    :return: True if the stock was bought successfully, False if the cash balance is not enough.
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.buy_stock({"name": "AAPL", "price": 150.0, "quantity": 10})
    True
    >>> tracker.portfolio
    [{'name': 'AAPL', 'price': 150.0, 'quantity': 10}]

    """
    total_cost = stock["price"] * stock["quantity"]
    
    if self.cash_balance >= total_cost:
        self.cash_balance -= total_cost
        
        # Check if stock already exists in portfolio
        existing_stock = None
        for s in self.portfolio:
            if s["name"] == stock["name"]:
                existing_stock = s
                break
        
        if existing_stock:
            # Update existing stock quantity and average price
            existing_stock["quantity"] += stock["quantity"]
        else:
            # Add new stock to portfolio
            self.portfolio.append(stock.copy())
        
        return True
    else:
        return False