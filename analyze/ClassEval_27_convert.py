def convert(self, amount, from_currency, to_currency):
    """
    एक दिए गए मुद्रा के मूल्य को दूसरे मुद्रा प्रकार में परिवर्तित करें
    :param amount: float, एक दिए गए मुद्रा का मूल्य
    :param from_currency: string, स्रोत मुद्रा प्रकार
    :param to_currency: string, लक्ष्य मुद्रा प्रकार
    :return: float, दूसरे मुद्रा प्रकार में परिवर्तित मूल्य
    >>> cc = CurrencyConverter()
    >>> cc.convert(64, 'CNY','USD')
    10.0
    """
    # Exchange rates relative to USD
    exchange_rates = {
        'USD': 1.0,
        'CNY': 6.4,
        'EUR': 0.85,
        'GBP': 0.75,
        'JPY': 110.0,
        'INR': 75.0,
        'AUD': 1.35,
        'CAD': 1.25
    }
    
    # Convert from source currency to USD, then from USD to target currency
    amount_in_usd = amount / exchange_rates[from_currency]
    converted_amount = amount_in_usd * exchange_rates[to_currency]
    
    return converted_amount