def add_currency_rate(self, currency, rate):
    """
        添加一个新的支持货币类型，如果该货币类型已经在支持列表中，则返回 False
        :param currency:字符串, 要添加的货币类型
        :param rate:浮点数, 该货币类型的汇率
        :return:如果成功，返回 None；如果不成功，返回 False
        >>> cc = CurrencyConverter()
        >>> cc.add_currency_rate('KRW', 1308.84)
        self.rates['KRW'] = 1308.84
        """
    if currency in self.rates:
        return False
    self.rates[currency] = rate