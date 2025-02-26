def normalized(self):
    """
    Return a version of this object represented entirely using integer
    values for the relative attributes.

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :return:
        Returns a :class:`dateutil.relativedelta.relativedelta` object.
    """
    total_hours = int(self.hours) + int(self.days * 24) + int(self.minutes / 60)
    total_days = int(self.days) + (total_hours // 24)
    total_hours = total_hours % 24

    return relativedelta(days=total_days, hours=total_hours)