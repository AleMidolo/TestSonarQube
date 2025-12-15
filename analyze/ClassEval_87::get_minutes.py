def get_minutes(self, string_time1, string_time2):
    """
    दो समयों के बीच कितने मिनट बीत चुके हैं, इसकी गणना करें, और परिणामों को निकटतम पूर्णांक में गोल करें
    :return: int, दो समयों के बीच मिनटों की संख्या, गोल किया हुआ
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    datetime1 = datetime.datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
    difference = (datetime2 - datetime1).total_seconds() / 60
    return round(difference)