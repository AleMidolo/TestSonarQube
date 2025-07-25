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

    # Convert all attributes to integers
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)
    years = int(self.years)
    months = int(self.months)
    weeks = int(self.weeks)

    # Handle fractional parts
    if hasattr(self, 'days') and self.days != days:
        hours += int((self.days - days) * 24)
    if hasattr(self, 'hours') and self.hours != hours:
        minutes += int((self.hours - hours) * 60)
    if hasattr(self, 'minutes') and self.minutes != minutes:
        seconds += int((self.minutes - minutes) * 60)
    if hasattr(self, 'seconds') and self.seconds != seconds:
        microseconds += int((self.seconds - seconds) * 1e6)

    return relativedelta(
        years=years,
        months=months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
        weeks=weeks
    )