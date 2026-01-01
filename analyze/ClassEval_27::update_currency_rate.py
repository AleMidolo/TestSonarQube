def update_currency_rate(self, currency, new_rate):
    """
        Actualiza el tipo de cambio para una cierta moneda
        :param currency:string
        :param new_rate:float
        :return:Si es exitoso, devuelve None; si no es exitoso, devuelve False
        >>> cc = CurrencyConverter()
        >>> cc.update_currency_rate('CNY', 7.18)
        self.rates['CNY'] = 7.18
        """
    if currency not in self.rates:
        return False
    self.rates[currency] = new_rate