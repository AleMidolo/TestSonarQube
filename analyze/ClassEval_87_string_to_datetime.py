def string_to_datetime(self, string):
    """
    将时间字符串转换为 datetime 实例
    :param string: 字符串, 转换格式之前的字符串
    :return: datetime 实例
    >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
    2001-07-18 01:01:01
    """
    from datetime import datetime
    
    # 尝试解析常见的日期时间格式
    formats = [
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S.%f",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M:%S.%f",
    ]
    
    # 首先尝试标准格式
    for fmt in formats:
        try:
            return datetime.strptime(string, fmt)
        except ValueError:
            continue
    
    # 如果标准格式失败，尝试处理不带前导零的格式（如示例中的 "2001-7-18 1:1:1"）
    # 将字符串标准化，添加前导零
    parts = string.split()
    if len(parts) == 2:
        date_part = parts[0]
        time_part = parts[1]
        
        # 处理日期部分
        date_components = date_part.replace('/', '-').split('-')
        if len(date_components) == 3:
            year, month, day = date_components
            date_part = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
        
        # 处理时间部分
        time_components = time_part.split(':')
        if len(time_components) == 3:
            hour, minute, second = time_components
            time_part = f"{hour.zfill(2)}:{minute.zfill(2)}:{second.zfill(2)}"
        
        normalized_string = f"{date_part} {time_part}"
        return datetime.strptime(normalized_string, "%Y-%m-%d %H:%M:%S")
    
    # 如果所有尝试都失败，使用dateutil作为后备
    try:
        from dateutil import parser
        return parser.parse(string)
    except:
        raise ValueError(f"无法解析时间字符串: {string}")