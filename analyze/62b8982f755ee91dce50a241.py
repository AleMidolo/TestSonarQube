def normalized(self):
    """
    将所有时间单位标准化为整数。

    返回一个完全使用整数值表示相对属性的对象版本。

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        返回一个 :class:`dateutil.relativedelta.relativedelta` 对象。
    """
    # 创建一个新的relativedelta对象来存储结果
    result = relativedelta()
    
    # 处理年和月,直接复制
    result.years = self.years
    result.months = self.months
    
    # 将天数转换为小时
    total_hours = self.hours + (self.days * 24)
    
    # 将小时转换为分钟
    total_minutes = self.minutes + (total_hours * 60)
    
    # 将分钟转换为秒
    total_seconds = self.seconds + (total_minutes * 60)
    
    # 将秒转换为微秒
    total_microseconds = self.microseconds + (total_seconds * 1000000)
    
    # 从微秒开始,逐级向上计算并取整
    result.microseconds = total_microseconds % 1000000
    remaining_seconds = total_microseconds // 1000000
    
    result.seconds = remaining_seconds % 60
    remaining_minutes = remaining_seconds // 60
    
    result.minutes = remaining_minutes % 60
    remaining_hours = remaining_minutes // 60
    
    result.hours = remaining_hours % 24
    result.days = remaining_hours // 24
    
    # 复制其他属性
    result.year = self.year
    result.month = self.month
    result.day = self.day
    result.weekday = self.weekday
    result.hour = self.hour
    result.minute = self.minute
    result.second = self.second
    result.microsecond = self.microsecond
    
    return result