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

    # 将天数和小时数转换为整数
    days = int(self.days)
    hours = int(self.hours) + int((self.days - days) * 24)
    minutes = int(self.minutes) + int((self.hours - int(self.hours)) * 60)
    seconds = int(self.seconds) + int((self.minutes - int(self.minutes)) * 60)
    microseconds = int(self.microseconds) + int((self.seconds - int(self.seconds)) * 1e6)

    # 处理可能的溢出
    if microseconds >= 1e6:
        seconds += microseconds // 1e6
        microseconds = microseconds % 1e6

    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60

    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60

    if hours >= 24:
        days += hours // 24
        hours = hours % 24

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