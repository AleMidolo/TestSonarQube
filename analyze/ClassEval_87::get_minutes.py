def get_minutes(self, string_time1, string_time2):
    """
        Calculate how many minutes have passed between two times, and round the results to the nearest
        :return: int, the number of minutes between two times, rounded off
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        60
        """
    dt1 = self.string_to_datetime(string_time1)
    dt2 = self.string_to_datetime(string_time2)
    time_difference = abs(dt2 - dt1)
    minutes = time_difference.total_seconds() / 60
    return round(minutes)