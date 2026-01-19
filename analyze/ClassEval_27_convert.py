def convert(self, amount, from_currency, to_currency):
    """
        एक दिए गए मुद्रा के मूल्य को दूसरे मुद्रा प्रकार में परिवर्तित करें
        :param amount: float, एक दिए गए मुद्रा का मूल्य
        :param from_currency: string, स्रोत मुद्रा प्रकार
        :param to_currency: string, लक्ष्य मुद्रा प्रकार
        :return: float, दूसरे मुद्रा प्रकार में परिवर्तित मूल्य
        >>> cc = CurrencyConverter()
        >>> cc.convert(64, 'CNY','USD')
        10.0
        """
    if from_currency not in self.rates or to_currency not in self.rates:
        raise ValueError('Unsupported currency type')
    amount_in_usd = amount / self.rates[from_currency]
    converted_amount = amount_in_usd * self.rates[to_currency]
    return converted_amount