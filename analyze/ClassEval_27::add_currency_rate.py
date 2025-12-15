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
        if from_currency == to_currency:
            return amount

        if from_currency not in self.rates or to_currency not in self.rates:
            return False

        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]

        converted_amount = (amount / from_rate) * to_rate
        return converted_amount

    def get_supported_currencies(self):
        """
        Returns a list of supported currency types
        :return:list, All supported currency types
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
        return list(self.rates.keys())

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