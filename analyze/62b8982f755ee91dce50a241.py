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

    # 将小数部分转换为整数
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)

    # 处理小数部分
    extra_hours = int((self.days - days) * 24)
    extra_minutes = int((self.hours - hours) * 60)
    extra_seconds = int((self.minutes - minutes) * 60)
    extra_microseconds = int((self.seconds - seconds) * 1e6)

    # 累加额外的时间
    hours += extra_hours
    minutes += extra_minutes
    seconds += extra_seconds
    microseconds += extra_microseconds

    # 处理进位
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

    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)