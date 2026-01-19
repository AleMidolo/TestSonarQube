def get_supported_currencies(self):
    """
    Devuelve una lista de tipos de moneda soportados
    :return:list, Todos los tipos de moneda soportados
    >>> cc = CurrencyConverter()
    >>> cc.get_supported_currencies()
    ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
    """
    return ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CNY']