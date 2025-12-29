def convert(self, amount, from_currency, to_currency):
    """
        Convert the value of a given currency to another currency type
        :param amount: float, The value of a given currency
        :param from_currency: string, source currency type
        :param to_currency: string, target currency type
        :return: float, value converted to another currency type
        >>> cc = CurrencyConverter()
        >>> cc.convert(64, 'CNY','USD')
        10.0
        """
    if from_currency not in self.rates or to_currency not in self.rates:
        raise ValueError('Unsupported currency type')
    amount_in_usd = amount / self.rates[from_currency]
    converted_amount = amount_in_usd * self.rates[to_currency]
    return converted_amount