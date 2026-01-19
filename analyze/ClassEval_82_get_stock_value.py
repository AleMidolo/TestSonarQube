def get_stock_value(self, stock):
    """
    एक स्टॉक का मूल्य प्राप्त करें।
    :param stock: एक डिक्शनरी जिसमें "name", "price", और "quantity" कुंजी हैं
    :return: स्टॉक का मूल्य, फ्लोट।
    >>> tracker = StockPortfolioTracker(10000.0)
    >>> tracker.get_stock_value({"name": "AAPL", "price": 150.0, "quantity": 10})
    1500.0

    """
    return float(stock["price"] * stock["quantity"])