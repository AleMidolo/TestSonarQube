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
    # This means 1 USD = 6.4 CNY
    
    # Define exchange rates relative to USD as base currency
    exchange_rates = {
        'USD': 1.0,
        'CNY': 6.4,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
        'CAD': 1.25,
        'AUD': 1.35
    }
    
    # Convert from source currency to USD, then from USD to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount