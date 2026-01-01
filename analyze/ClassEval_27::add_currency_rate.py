def add_currency_rate(self, currency, rate):
    """
        एक नया समर्थित मुद्रा प्रकार जोड़ें, यदि मुद्रा प्रकार पहले से समर्थन सूची में है तो False लौटाएं
        :param currency:string, जो मुद्रा प्रकार जोड़ा जाना है
        :param rate:float, इस मुद्रा प्रकार के लिए विनिमय दर
        :return: यदि सफल, तो None लौटाता है; यदि असफल, तो False लौटाता है
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        """
    if currency in self.rates:
        return False
    self.rates[currency] = rate