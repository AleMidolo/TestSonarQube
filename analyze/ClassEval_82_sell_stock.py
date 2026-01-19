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
    stock_name = stock['name']
    sell_quantity = stock['quantity']
    sell_price = stock['price']
    
    # Find the stock in portfolio
    for i, portfolio_stock in enumerate(self.portfolio):
        if portfolio_stock['name'] == stock_name:
            # Check if we have enough quantity to sell
            if portfolio_stock['quantity'] < sell_quantity:
                return False
            
            # Calculate cash to add
            cash_to_add = sell_price * sell_quantity
            self.cash_balance += cash_to_add
            
            # Update or remove stock from portfolio
            if portfolio_stock['quantity'] == sell_quantity:
                # Remove stock completely
                self.portfolio.pop(i)
            else:
                # Reduce quantity
                portfolio_stock['quantity'] -= sell_quantity
            
            return True
    
    # Stock not found in portfolio
    return False