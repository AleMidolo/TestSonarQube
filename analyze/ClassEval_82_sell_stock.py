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
    
    # पोर्टफोलियो में स्टॉक खोजें
    for i, portfolio_stock in enumerate(self.portfolio):
        if portfolio_stock['name'] == name:
            # जांचें कि पर्याप्त मात्रा है या नहीं
            if portfolio_stock['quantity'] < quantity:
                return False
            
            # नकद बैलेंस में जोड़ें
            self.cash_balance += price * quantity
            
            # स्टॉक की मात्रा घटाएं
            portfolio_stock['quantity'] -= quantity
            
            # यदि मात्रा 0 हो जाती है, तो पोर्टफोलियो से हटा दें
            if portfolio_stock['quantity'] == 0:
                self.portfolio.pop(i)
            
            return True
    
    # यदि स्टॉक पोर्टफोलियो में नहीं मिला
    return False