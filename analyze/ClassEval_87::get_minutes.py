def get_minutes(self, string_time1, string_time2):
    """
    计算两个时间之间经过了多少分钟，并将结果四舍五入到最接近的整数
    :return: int, 两个时间之间的分钟数，四舍五入
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    
    datetime1 = self.string_to_datetime(string_time1)
    datetime2 = self.string_to_datetime(string_time2)
    delta = datetime2 - datetime1
    return round(delta.total_seconds() / 60)