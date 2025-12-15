def update_currency_rate(self, currency, new_rate):
        """
        एक निश्चित मुद्रा के लिए विनिमय दर को अपडेट करें
        :param currency:string
        :param new_rate:float
        :return:यदि सफल, तो None लौटाता है; यदि असफल, तो False लौटाता है
        >>> cc = CurrencyConverter()
        >>> cc.update_currency_rate('CNY', 7.18)
        self.rates['CNY'] = 7.18
        """
        if currency not in self.rates:
            return False
        self.rates[currency] = new_rate