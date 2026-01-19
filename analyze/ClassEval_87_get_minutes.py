def get_minutes(self, string_time1, string_time2):
    """
    दो समयों के बीच कितने मिनट बीत चुके हैं, इसकी गणना करें, और परिणामों को निकटतम पूर्णांक में गोल करें
    :return: int, दो समयों के बीच मिनटों की संख्या, गोल किया हुआ
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    from datetime import datetime
    
    # Parse the time strings to datetime objects
    time1 = datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
    
    # Calculate the difference
    time_diff = abs(time2 - time1)
    
    # Convert to minutes and round to nearest integer
    minutes = round(time_diff.total_seconds() / 60)
    
    return minutes