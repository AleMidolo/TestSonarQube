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
    
    # 处理年和月,直接复制整数部分
    result.years = int(self.years)
    result.months = int(self.months)
    
    # 计算总秒数
    total_seconds = (
        self.days * 86400 +  # 天转秒
        self.hours * 3600 +  # 小时转秒
        self.minutes * 60 +  # 分钟转秒
        self.seconds         # 秒
    )
    
    # 从总秒数中提取各个时间单位
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # 设置标准化后的值
    result.days = int(days)
    result.hours = int(hours)
    result.minutes = int(minutes)
    result.seconds = int(seconds)
    
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