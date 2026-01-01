@staticmethod
def BulkItemPromo(order):
    """
        आदेश में थोक आइटम की मात्रा के आधार पर छूट की गणना करें। यदि एक ही आइटम की मात्रा 20 या उससे अधिक हो जाती है, तो प्रत्येक आइटम को 10% छूट मिलेगी।
        :param order: ऑब्जेक्ट, जिस पर छूट लागू करनी है
        :return: फ्लोट, छूट की राशि
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 20, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.BulkItemPromo)
        >>> DiscountStrategy.BulkItemPromo(order)
        47.0

        """
    discount = 0
    for item in order.cart:
        if item['quantity'] >= 20:
            discount += item['quantity'] * item['price'] * 0.1
    return discount