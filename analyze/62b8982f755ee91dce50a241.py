from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    Return a version of this object represented entirely using integer
    values for the relative attributes.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Returns a :class:`dateutil.relativedelta.relativedelta` object.
    """
    total_days = int(self.days) + int(self.hours // 24)
    total_hours = int(self.hours % 24) + int((self.minutes + self.seconds / 60) // 60)
    total_minutes = int((self.minutes + self.seconds / 60) % 60)
    total_seconds = int(self.seconds % 60)

    return relativedelta(days=total_days, hours=total_hours, minutes=total_minutes, seconds=total_seconds)