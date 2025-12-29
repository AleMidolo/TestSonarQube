def convert(self, amount, from_currency, to_currency):
    """
        将给定货币的值转换为另一种货币类型
        :param amount: 浮点数, 给定货币的值
        :param from_currency: 字符串, 源货币类型
        :param to_currency: 字符串, 目标货币类型
        :return: 浮点数, 转换为另一种货币类型的值
        >>> cc = CurrencyConverter()
        >>> cc.convert(64, 'CNY','USD')
        10.0
        """
    if from_currency not in self.rates or to_currency not in self.rates:
        raise ValueError(f'Unsupported currency. Supported currencies: {list(self.rates.keys())}')
    amount_in_usd = amount / self.rates[from_currency]
    converted_amount = amount_in_usd * self.rates[to_currency]
    return converted_amount