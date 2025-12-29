def string_to_datetime(self, string):
    """
        将时间字符串转换为 datetime 实例
        :param string: 字符串, 转换格式之前的字符串
        :return: datetime 实例
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%Y.%m.%d %H:%M:%S', '%Y.%m.%d %H:%M', '%Y.%m.%d']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    normalized = string.strip()
    try:
        from dateutil import parser
        return parser.parse(normalized)
    except ImportError:
        parts = normalized.split()
        date_part = parts[0]
        time_part = parts[1] if len(parts) > 1 else '00:00:00'
        for sep in ['-', '/', '.']:
            date_part = date_part.replace(sep, '-')
        date_parts = date_part.split('-')
        if len(date_parts) == 3:
            year, month, day = map(int, date_parts)
        else:
            raise ValueError(f'Unable to parse date string: {string}')
        time_parts = time_part.split(':')
        if len(time_parts) == 3:
            hour, minute, second = map(int, time_parts)
        elif len(time_parts) == 2:
            hour, minute = map(int, time_parts)
            second = 0
        elif len(time_parts) == 1:
            hour = int(time_parts[0])
            minute = second = 0
        else:
            hour = minute = second = 0
        return datetime.datetime(year, month, day, hour, minute, second)