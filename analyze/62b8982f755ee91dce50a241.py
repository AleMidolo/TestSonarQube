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

    # Convert all attributes to integers
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)

    # Handle fractional parts
    fractional_days = self.days - days
    if fractional_days != 0:
        hours += int(fractional_days * 24)
        fractional_hours = (fractional_days * 24) - int(fractional_days * 24)
        if fractional_hours != 0:
            minutes += int(fractional_hours * 60)
            fractional_minutes = (fractional_hours * 60) - int(fractional_hours * 60)
            if fractional_minutes != 0:
                seconds += int(fractional_minutes * 60)
                fractional_seconds = (fractional_minutes * 60) - int(fractional_minutes * 60)
                if fractional_seconds != 0:
                    microseconds += int(fractional_seconds * 1e6)

    # Normalize the time units
    carry, seconds = divmod(seconds, 60)
    minutes += carry
    carry, minutes = divmod(minutes, 60)
    hours += carry
    carry, hours = divmod(hours, 24)
    days += carry

    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)