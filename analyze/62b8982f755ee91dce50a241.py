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

    # 将天数的浮点部分转换为小时
    days = int(self.days)
    hours = self.hours + (self.days - days) * 24

    # 将小时的浮点部分转换为分钟
    hours = int(hours)
    minutes = self.minutes + (hours - int(hours)) * 60

    # 将分钟的浮点部分转换为秒
    minutes = int(minutes)
    seconds = self.seconds + (minutes - int(minutes)) * 60

    # 将秒的浮点部分转换为微秒
    seconds = int(seconds)
    microseconds = self.microseconds + (seconds - int(seconds)) * 1e6

    # 返回标准化后的 relativedelta 对象
    return relativedelta(
        years=self.years,
        months=self.months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=int(microseconds),
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        weekday=self.weekday,
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=int(self.microsecond)
    )