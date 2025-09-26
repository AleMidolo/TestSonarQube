class CurrencyConverter:
    def __init__(self):
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
        if self._is_same_currency(from_currency, to_currency):
            return amount

        if not self._are_currencies_supported(from_currency, to_currency):
            return False

        return self._convert_amount(amount, from_currency, to_currency)

    def _is_same_currency(self, from_currency, to_currency):
        return from_currency == to_currency

    def _are_currencies_supported(self, from_currency, to_currency):
        return from_currency in self.rates and to_currency in self.rates

    def _convert_amount(self, amount, from_currency, to_currency):
        from_rate = self.rates[from_currency]
        to_rate = self.rates[to_currency]
        return (amount / from_rate) * to_rate

    def get_supported_currencies(self):
        return list(self.rates.keys())

    def add_currency_rate(self, currency, rate):
        if currency in self.rates:
            return False
        self.rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate