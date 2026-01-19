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
    # 假设存在一个汇率字典，存储各货币相对于基准货币(如USD)的汇率
    # 根据示例: 64 CNY = 10 USD, 所以 1 USD = 6.4 CNY
    if not hasattr(self, 'rates'):
        # 默认汇率表 (相对于USD)
        self.rates = {
            'USD': 1.0,
            'CNY': 6.4,
            'EUR': 0.85,
            'GBP': 0.73,
            'JPY': 110.0
        }
    
    # 先转换为USD，再转换为目标货币
    amount_in_usd = amount / self.rates[from_currency]
    result = amount_in_usd * self.rates[to_currency]
    
    return result