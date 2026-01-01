def convert(self, amount, from_currency, to_currency):
    """
        Convierte el valor de una moneda dada a otro tipo de moneda
        :param amount: float, El valor de una moneda dada
        :param from_currency: string, tipo de moneda de origen
        :param to_currency: string, tipo de moneda de destino
        :return: float, valor convertido a otro tipo de moneda
        >>> cc = CurrencyConverter()
        >>> cc.convert(64, 'CNY','USD')
        10.0
        """
    if from_currency not in self.rates or to_currency not in self.rates:
        raise ValueError('Unsupported currency')
    amount_in_usd = amount / self.rates[from_currency]
    converted_amount = amount_in_usd * self.rates[to_currency]
    return converted_amount