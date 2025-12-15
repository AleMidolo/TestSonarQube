class CurrencyConverter: 
    def __init__(self):
        """
        Initialize the exchange rate of the US dollar against various currencies
        """
        self.rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
        return list(self.rates.keys())
    
    def add_currency_rate(self, currency, rate):
        """
        Add a new supported currency type, return False if the currency type is already in the support list
        :param currency:string, currency type to be added
        :param rate:float, exchange rate for this type of currency
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        self.rates['KRW'] = 1308.84
        """
        if currency in self.rates:
            return False
        self.rates[currency] = rate
    
    def update_currency_rate(self, currency, new_rate):
        """
        Update the exchange rate for a certain currency
        :param currency:string
        :param new_rate:float
        :return:If successful, returns None; if unsuccessful, returns False
        >>> cc = CurrencyConverter()
        >>> cc.update_currency_rate('CNY', 7.18)
        self.rates['CNY'] = 7.18
        """
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate
    
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
        if from_currency not in self.rates or to_currency not in self.rates:
            raise ValueError("Unsupported currency type")
        
        # Convert amount to USD first
        amount_in_usd = amount / self.rates[from_currency]
        # Convert USD to target currency
        converted_amount = amount_in_usd * self.rates[to_currency]
        
        return converted_amount