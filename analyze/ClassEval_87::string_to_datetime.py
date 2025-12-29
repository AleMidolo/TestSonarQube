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
    normalized = string.strip()
    try:
        from dateutil import parser
        return parser.parse(normalized)
    except ImportError:
        parts = normalized.replace('-', ' ').replace(':', ' ').replace('/', ' ').replace('.', ' ').split()
        if len(parts) >= 3:
            try:
                year = int(parts[0])
                month = int(parts[1])
                day = int(parts[2])
                hour = minute = second = 0
                if len(parts) >= 4:
                    hour = int(parts[3])
                if len(parts) >= 5:
                    minute = int(parts[4])
                if len(parts) >= 6:
                    second = int(parts[5])
                return datetime.datetime(year, month, day, hour, minute, second)
            except (ValueError, IndexError):
                pass
        raise ValueError(f'Unable to parse time string: {string}')