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

    # 将天数的浮点数部分转换为小时
    days_fractional, days_integral = math.modf(self.days)
    hours_from_days = days_fractional * 24

    # 将小时数的浮点数部分转换为分钟
    hours_fractional, hours_integral = math.modf(self.hours + hours_from_days)
    minutes_from_hours = hours_fractional * 60

    # 将分钟数的浮点数部分转换为秒
    minutes_fractional, minutes_integral = math.modf(self.minutes + minutes_from_hours)
    seconds_from_minutes = minutes_fractional * 60

    # 将秒数的浮点数部分转换为微秒
    seconds_fractional, seconds_integral = math.modf(self.seconds + seconds_from_minutes)
    microseconds_from_seconds = seconds_fractional * 1e6

    # 将微秒数的浮点数部分舍去
    microseconds_integral = int(microseconds_from_seconds + self.microseconds)

    # 创建新的 relativedelta 对象
    return relativedelta(
        years=self.years,
        months=self.months,
        days=int(days_integral),
        hours=int(hours_integral),
        minutes=int(minutes_integral),
        seconds=int(seconds_integral),
        microseconds=microseconds_integral,
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=self.microsecond
    )