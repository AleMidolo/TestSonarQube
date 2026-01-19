def buy_stock(self, stock):
    """
    एक स्टॉक खरीदें और इसे पोर्टफोलियो में जोड़ें।
    :param stock: एक डिक्शनरी जिसमें "name", "price", और "quantity" की कुंजी हैं
    :param quantity: खरीदने के लिए स्टॉक की मात्रा, int.
    :return: यदि स्टॉक सफलतापूर्वक खरीदा गया तो True, यदि नकद बैलेंस पर्याप्त नहीं है तो False.
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
        found = False
        for existing_stock in self.portfolio:
            if existing_stock["name"] == stock["name"]:
                existing_stock["quantity"] += stock["quantity"]
                found = True
                break
        
        # If stock doesn't exist, add it to portfolio
        if not found:
            self.portfolio.append(stock.copy())
        
        return True
    else:
        return False