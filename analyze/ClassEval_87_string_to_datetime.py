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
    import re
    
    # 分离日期和时间部分
    parts = string.strip().split()
    if len(parts) >= 1:
        date_part = parts[0]
        time_part = parts[1] if len(parts) > 1 else "0:0:0"
        
        # 处理日期部分（支持 - 或 / 分隔符）
        if '-' in date_part:
            date_components = date_part.split('-')
            separator = '-'
        else:
            date_components = date_part.split('/')
            separator = '/'
        
        # 补齐日期部分的前导零
        if len(date_components) == 3:
            year, month, day = date_components
            date_part = f"{year.zfill(4)}{separator}{month.zfill(2)}{separator}{day.zfill(2)}"
        
        # 处理时间部分
        time_components = time_part.split(':')
        if len(time_components) >= 2:
            hour = time_components[0].zfill(2)
            minute = time_components[1].zfill(2)
            second = time_components[2].zfill(2) if len(time_components) > 2 else "00"
            time_part = f"{hour}:{minute}:{second}"
        
        normalized_string = f"{date_part} {time_part}"
        return datetime.strptime(normalized_string, "%Y{0}%m{0}%d %H:%M:%S".format(separator))
    
    raise ValueError(f"Unable to parse datetime string: {string}")