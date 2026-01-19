def get_minutes(self, string_time1, string_time2):
    """
    计算两个时间之间经过了多少分钟，并将结果四舍五入到最接近的整数
    :return: int, 两个时间之间的分钟数，四舍五入
    >>> timeutils.get_minutes("2001-7-18 1:1:1", "2001-7-18 2:1:1")
    60
    """
    from datetime import datetime
    
    # 解析时间字符串
    time1 = datetime.strptime(string_time1, "%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(string_time2, "%Y-%m-%d %H:%M:%S")
    
    # 计算时间差
    time_diff = abs(time2 - time1)
    
    # 转换为分钟并四舍五入
    minutes = round(time_diff.total_seconds() / 60)
    
    return minutes