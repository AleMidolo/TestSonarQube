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
    # 定义汇率字典，以USD为基准
    exchange_rates = {
        'USD': 1.0,
        'CNY': 6.4,
        'EUR': 0.85,
        'GBP': 0.73,
        'JPY': 110.0,
    }
    
    # 如果源货币和目标货币相同，直接返回原值
    if from_currency == to_currency:
        return float(amount)
    
    # 先转换为USD（基准货币），再转换为目标货币
    # amount in from_currency -> USD -> to_currency
    amount_in_usd = amount / exchange_rates[from_currency]
    result = amount_in_usd * exchange_rates[to_currency]
    
    return result