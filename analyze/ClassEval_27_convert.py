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
    # Tasas de cambio relativas al USD
    exchange_rates = {
        'USD': 1.0,
        'CNY': 6.4,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0,
        'CAD': 1.25,
        'AUD': 1.35,
        'CHF': 0.92,
        'INR': 74.0,
        'MXN': 20.0
    }
    
    # Convertir de from_currency a USD, luego de USD a to_currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount