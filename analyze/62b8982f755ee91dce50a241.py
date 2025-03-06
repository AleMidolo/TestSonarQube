def normalized(self):
    """
    将所有时间单位标准化为整数。

    返回一个完全使用整数值表示相对属性的对象版本。

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
      返回一个 :class:`dateutil.relativedelta.relativedelta` 对象。
    """
    from dateutil.relativedelta import relativedelta
    import math

    # 将天数和小时数转换为整数
    days = int(self.days)
    hours = int(self.hours)
    
    # 处理小数部分
    fractional_days = self.days - days
    fractional_hours = self.hours - hours
    
    # 将小数部分转换为小时
    additional_hours = int(fractional_days * 24 + fractional_hours)
    
    # 更新小时数
    hours += additional_hours
    
    # 处理小时数超过24小时的情况
    if hours >= 24:
        days += hours // 24
        hours = hours % 24
    
    # 返回标准化后的relativedelta对象
    return relativedelta(days=days, hours=hours)