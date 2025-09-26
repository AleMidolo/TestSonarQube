class CurrencyConverter:
    def __init__(self):
        self._rates = {
            'USD': 1.0,
            'EUR': 0.85,
            'GBP': 0.72,
            'JPY': 110.15,
            'CAD': 1.23,
            'AUD': 1.34,
            'CNY': 6.40,
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount

        if not self._is_currency_supported(from_currency) or not self._is_currency_supported(to_currency):
            return False

        from_rate = self._get_currency_rate(from_currency)
        to_rate = self._get_currency_rate(to_currency)

        return self._calculate_converted_amount(amount, from_rate, to_rate)

    def get_supported_currencies(self):
        return list(self._rates.keys())

    def add_currency_rate(self, currency, rate):
        if self._is_currency_supported(currency):
            return False
        self._rates[currency] = rate

    def update_currency_rate(self, currency, new_rate):
        if not self._is_currency_supported(currency):
            return False
        self._rates[currency] = new_rate

    def _is_currency_supported(self, currency):
        return currency in self._rates

    def _get_currency_rate(self, currency):
        return self._rates[currency]

    def _calculate_converted_amount(self, amount, from_rate, to_rate):
        return (amount / from_rate) * to_rate