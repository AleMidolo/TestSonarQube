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

    # 将天数和小时数标准化为整数
    days = int(self.days)
    hours = self.hours + (self.days - days) * 24
    hours = int(hours)
    
    # 将小时数和分钟数标准化为整数
    minutes = self.minutes + (hours - int(hours)) * 60
    minutes = int(minutes)
    
    # 将分钟数和秒数标准化为整数
    seconds = self.seconds + (minutes - int(minutes)) * 60
    seconds = int(seconds)
    
    # 将秒数和微秒数标准化为整数
    microseconds = self.microseconds + (seconds - int(seconds)) * 1e6
    microseconds = int(microseconds)
    
    # 返回标准化后的 relativedelta 对象
    return relativedelta(
        years=self.years,
        months=self.months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        weekday=self.weekday,
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=self.microsecond
    )