def string_to_datetime(self, string):
    """
        将时间字符串转换为 datetime 实例
        :param string: 字符串, 转换格式之前的字符串
        :return: datetime 实例
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%Y.%m.%d %H:%M:%S', '%Y.%m.%d %H:%M', '%Y.%m.%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%d.%m.%Y %H:%M:%S', '%d.%m.%Y %H:%M', '%d.%m.%Y']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    string = string.strip()
    try:
        if ' ' in string:
            date_part, time_part = string.split(' ', 1)
        else:
            date_part = string
            time_part = '00:00:00'
        date_parts = date_part.replace('-', ' ').replace('/', ' ').replace('.', ' ').split()
        year = int(date_parts[0])
        month = int(date_parts[1])
        day = int(date_parts[2])
        time_parts = time_part.replace(':', ' ').split()
        if len(time_parts) == 3:
            hour = int(time_parts[0])
            minute = int(time_parts[1])
            second = int(time_parts[2])
        elif len(time_parts) == 2:
            hour = int(time_parts[0])
            minute = int(time_parts[1])
            second = 0
        elif len(time_parts) == 1:
            hour = int(time_parts[0])
            minute = 0
            second = 0
        else:
            hour = minute = second = 0
        return datetime.datetime(year, month, day, hour, minute, second)
    except (ValueError, IndexError):
        raise ValueError(f'Unable to parse time string: {string}')