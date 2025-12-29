def total(self):
    """
        कार्ट में आइटम्स की कुल लागत की गणना करें।
        :return: float, आइटम्स की कुल लागत
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> ds = DiscountStrategy(customer, cart)
        >>> ds.total()
        329.0

        """
    return sum((item['quantity'] * item['price'] for item in self.cart))