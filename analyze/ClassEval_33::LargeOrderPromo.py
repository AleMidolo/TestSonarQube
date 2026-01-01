@staticmethod
def LargeOrderPromo(order):
    """
        ऑर्डर में विभिन्न उत्पादों की संख्या के आधार पर छूट की गणना करें। यदि ऑर्डर में विभिन्न उत्पादों की मात्रा 10 या उससे अधिक हो जाती है, तो पूरे ऑर्डर पर 7% की छूट मिलेगी।
        :param order: ऑब्जेक्ट, जिस पर छूट लागू की जानी है
        :return: फ्लोट, छूट की राशि
        >>> customer = {'name': 'John Doe', 'fidelity': 1200}
        >>> cart = [{'product': 'product', 'quantity': 14, 'price': 23.5}]
        >>> order = DiscountStrategy(customer, cart, DiscountStrategy.LargeOrderPromo)
        >>> DiscountStrategy.LargeOrderPromo(order)
        0.0

        """
    return order.total() * 0.07 if len(order.cart) >= 10 else 0