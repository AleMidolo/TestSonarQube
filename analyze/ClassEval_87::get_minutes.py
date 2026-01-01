def get_minutes(self, string_time1, string_time2):
    """
        दो समयों के बीच कितने मिनट बीत चुके हैं, इसकी गणना करें, और परिणामों को निकटतम पूर्णांक में गोल करें
        :return: int, दो समयों के बीच मिनटों की संख्या, गोल किया हुआ
        >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
        60
        """
    dt1 = self.string_to_datetime(string_time1)
    dt2 = self.string_to_datetime(string_time2)
    time_difference = abs(dt2 - dt1)
    minutes = time_difference.total_seconds() / 60
    return round(minutes)