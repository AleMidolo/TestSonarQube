def update_currency_rate(self, currency, new_rate):
    """
    Aggiorna il tasso di cambio per una certa valuta
    :param currency:string
    :param new_rate:float
    :return:Se ha successo, restituisce None; se non ha successo, restituisce False
    >>> cc = CurrencyConverter()
    >>> cc.update_currency_rate('CNY', 7.18)
    self.rates['CNY'] = 7.18
    """
    if currency in self.rates:
        self.rates[currency] = new_rate
        return None
    else:
        return False