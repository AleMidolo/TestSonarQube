def get_supported_currencies(self):
    """
        समर्थित मुद्रा प्रकारों की सूची लौटाता है
        :return:list, सभी समर्थित मुद्रा प्रकार
        >>> cc = CurrencyConverter()
        >>> cc.get_supported_currencies()
        ['USD','EUR','GBP','JPY','CAD','AUD','CNY']
        """
    return list(self.rates.keys())