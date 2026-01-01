def get_supported_currencies(self):
    """
        Restituisce un elenco dei tipi di valuta supportati
        :return:list, Tutti i tipi di valuta supportati
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
    return list(self.rates.keys())