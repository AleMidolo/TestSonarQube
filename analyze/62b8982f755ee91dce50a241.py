from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    将所有时间单位标准化为整数。

    返回一个完全使用整数值表示相对属性的对象版本。

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        返回一个 :class:`dateutil.relativedelta.relativedelta` 对象。
    """
    total_days = int(self.days) + int(self.hours // 24)
    total_hours = int(self.hours % 24)
    total_minutes = int(self.minutes)
    total_seconds = int(self.seconds)

    return relativedelta(days=total_days, hours=total_hours, minutes=total_minutes, seconds=total_seconds)