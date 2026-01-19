def string_to_datetime(self, string):
    """
    将时间字符串转换为 datetime 实例
    :param string: 字符串, 转换格式之前的字符串
    :return: datetime 实例
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # 尝试多种常见的日期时间格式
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S.%f",
        "%Y-%m-%d",
        "%Y/%m/%d",
    ]
    
    # 首先尝试标准格式
    for fmt in formats:
        try:
            return datetime.strptime(string, fmt)
        except ValueError:
            continue
    
    # 如果标准格式都失败，尝试处理不规则格式（如 "2001-7-18 1:1:1"）
    # 将单个数字的月、日、时、分、秒补零
    import re
    
    # 匹配日期时间模式并规范化
    pattern = r'(\d{4})[/-](\d{1,2})[/-](\d{1,2})(?:\s+(\d{1,2}):(\d{1,2}):(\d{1,2})(?:\.(\d+))?)?'
    match = re.match(pattern, string.strip())
    
    if match:
        year, month, day, hour, minute, second, microsecond = match.groups()
        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour) if hour else 0
        minute = int(minute) if minute else 0
        second = int(second) if second else 0
        microsecond = int(microsecond.ljust(6, '0')[:6]) if microsecond else 0
        
        return datetime(year, month, day, hour, minute, second, microsecond)
    
    # 如果所有方法都失败，抛出异常
    raise ValueError(f"Unable to parse datetime string: {string}")