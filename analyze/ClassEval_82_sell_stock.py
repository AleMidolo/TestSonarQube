def sell_stock(self, stock):
    """
    एक स्टॉक बेचें और इसे पोर्टफोलियो से हटा दें और नकद को नकद बैलेंस में जोड़ें।
    :param stock: एक शब्दकोश जिसमें कुंजी "name", "price", और "quantity" हैं
    :param quantity: बेचे जाने वाले स्टॉक की मात्रा, int.
    :return: True यदि स्टॉक सफलतापूर्वक बेचा गया, False यदि स्टॉक की मात्रा पर्याप्त नहीं है।
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
    
    # Find the stock in portfolio
    for i, portfolio_stock in enumerate(self.portfolio):
        if portfolio_stock['name'] == name:
            # Check if we have enough quantity to sell
            if portfolio_stock['quantity'] >= quantity:
                # Add cash from sale
                self.cash_balance += price * quantity
                
                # Update or remove stock from portfolio
                portfolio_stock['quantity'] -= quantity
                
                # If quantity becomes 0, remove from portfolio
                if portfolio_stock['quantity'] == 0:
                    self.portfolio.pop(i)
                
                return True
            else:
                # Not enough quantity to sell
                return False
    
    # Stock not found in portfolio
    return False