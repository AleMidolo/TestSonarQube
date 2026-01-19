def convert(self, amount, from_currency, to_currency):
    """
    Convertire il valore di una valuta data in un altro tipo di valuta
    :param amount: float, Il valore di una valuta data
    :param from_currency: string, tipo di valuta di origine
    :param to_currency: string, tipo di valuta di destinazione
    :return: float, valore convertito in un altro tipo di valuta
    >>> cc = CurrencyConverter()
    >>> cc.convert(64, 'CNY','USD')
    10.0
    """
    # Assuming exchange rates are stored in self.rates dictionary
    # with USD as the base currency
    if not hasattr(self, 'rates'):
        # Default exchange rates (example rates relative to USD)
        self.rates = {
            'USD': 1.0,
            'CNY': 6.4,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 110.0
        }
    
    # Convert from_currency to USD, then USD to to_currency
    amount_in_usd = amount / self.rates[from_currency]
    converted_amount = amount_in_usd * self.rates[to_currency]
    
    return converted_amount