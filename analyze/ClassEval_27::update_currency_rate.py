def update_currency_rate(self, currency, new_rate):
    """
    更新某种货币的汇率
    :param currency: 字符串
    :param new_rate: 浮点数
    :return: 如果成功，返回 None；如果不成功，返回 False
    >>> cc = CurrencyConverter()
    >>> cc.update_currency_rate('CNY', 7.18)
    self.rates['CNY'] = 7.18
    """
    if currency not in self.rates:
        return False
    self.rates[currency] = new_rate