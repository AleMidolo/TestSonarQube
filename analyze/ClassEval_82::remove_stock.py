def remove_stock(self, stock):
        """
        पोर्टफोलियो से एक स्टॉक हटाएं।
        :param stock: एक शब्दकोश जिसमें "name", "price", और "quantity" कुंजी हैं
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