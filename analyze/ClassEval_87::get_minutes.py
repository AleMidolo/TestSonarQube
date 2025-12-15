def get_minutes(self, string_time1, string_time2):
    """
    Calculate how many minutes have passed between two times, and round the results to the nearest
    :return: int, the number of minutes between two times, rounded off
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    datetime1 = datetime.datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
    delta = datetime2 - datetime1
    return round(delta.total_seconds() / 60)