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
    for pf in self.portfolio:
        if pf['name'] == stock['name'] and pf['quantity'] >= stock['quantity']:
            pf['quantity'] -= stock['quantity']
            self.cash_balance += stock['price'] * stock['quantity']
            if pf['quantity'] == 0:
                self.portfolio.remove(pf)
            return True
    return False