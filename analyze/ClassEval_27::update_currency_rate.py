def update_currency_rate(self, currency, new_rate):
    """
    Update the exchange rate of a given currency
    :param currency: string, currency type to be updated
    :param new_rate: float, new exchange rate for this currency type
    :return: If successful, returns None; if unsuccessful, returns False
    >>> cc = CurrencyConverter()
    >>> cc.update_currency_rate('CNY', 7.18)
    self.rates['CNY'] = 7.18
    """
    
    if currency not in self.rates:
        return False
    self.rates[currency] = new_rate