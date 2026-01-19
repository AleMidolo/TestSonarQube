def convert(self, amount, from_currency, to_currency):
    """
    Convert the value of a given currency to another currency type
    :param amount: float, The value of a given currency
    :param from_currency: string, source currency type
    :param to_currency: string, target currency type
    :return: float, value converted to another currency type
    >>> cc = CurrencyConverter()
    >>> cc.convert(64, 'CNY','USD')
    10.0
    """
    # Based on the example: 64 CNY = 10 USD
    # This implies CNY to USD rate is 10/64 = 0.15625
    # Or USD to CNY rate is 64/10 = 6.4
    
    # Define exchange rates relative to USD as base currency
    rates = {
        'USD': 1.0,
        'CNY': 6.4,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
        'CAD': 1.25,
        'AUD': 1.35
    }
    
    # Convert from source currency to USD, then from USD to target currency
    amount_in_usd = amount / rates[from_currency]
    result = amount_in_usd * rates[to_currency]
    
    return result