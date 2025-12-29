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
    if from_currency not in self.rates or to_currency not in self.rates:
        raise ValueError('Unsupported currency')
    amount_in_usd = amount / self.rates[from_currency]
    converted_amount = amount_in_usd * self.rates[to_currency]
    return converted_amount