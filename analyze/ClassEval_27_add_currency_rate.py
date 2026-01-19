def add_currency_rate(self, currency, rate):
    """
        Agrega un nuevo tipo de moneda soportada, devuelve False si el tipo de moneda ya está en la lista de soporte
        :param currency:string, tipo de moneda a ser agregado
        :param rate:float, tasa de cambio para este tipo de moneda
        :return: Si es exitoso, devuelve None; si no es exitoso, devuelve False
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        """
    if currency in self.rates:
        return False
    self.rates[currency] = rate