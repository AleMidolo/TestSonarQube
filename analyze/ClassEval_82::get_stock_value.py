def get_stock_value(self, stock):
    """
        获取股票的价值。
        :param stock: 一个字典，包含键 "name"、"price" 和 "quantity"
        :return: 股票的价值，浮点数。
        >>> tracker = StockPortfolioTracker(10000.0)
        >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
        1500.0

        """
    return stock['price'] * stock['quantity']