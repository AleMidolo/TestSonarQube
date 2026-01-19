def add_currency_rate(self, currency, rate):
    """
    Aggiungi un nuovo tipo di valuta supportata, restituisce False se il tipo di valuta è già nella lista di supporto
    :param currency:string, tipo di valuta da aggiungere
    :param rate:float, tasso di cambio per questo tipo di valuta
    :return:Se ha successo, restituisce None; se non ha successo, restituisce False
    >>> cc = CurrencyConverter()
    >>> cc.add_currency_rate('KRW', 1308.84)
    self.rates['KRW'] = 1308.84
    """
    if currency in self.rates:
        return False
    self.rates[currency] = rate
    return None