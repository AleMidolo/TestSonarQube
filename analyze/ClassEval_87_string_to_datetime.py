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
        try:
            for sep in [' ', 'T']:
                if sep in normalized:
                    date_part, time_part = normalized.split(sep, 1)
                    break
            else:
                date_part = normalized
                time_part = '00:00:00'
            for date_sep in ['-', '/', '.']:
                if date_sep in date_part:
                    date_parts = date_part.split(date_sep)
                    if len(date_parts) == 3:
                        try:
                            year = int(date_parts[0])
                            month = int(date_parts[1])
                            day = int(date_parts[2])
                            if year < 100:
                                year += 2000 if year < 50 else 1900
                        except ValueError:
                            try:
                                day = int(date_parts[0])
                                month = int(date_parts[1])
                                year = int(date_parts[2])
                                if year < 100:
                                    year += 2000 if year < 50 else 1900
                            except ValueError:
                                continue
                        time_parts = time_part.split(':')
                        hour = int(time_parts[0]) if len(time_parts) > 0 else 0
                        minute = int(time_parts[1]) if len(time_parts) > 1 else 0
                        second = int(time_parts[2]) if len(time_parts) > 2 else 0
                        return datetime.datetime(year, month, day, hour, minute, second)
        except (ValueError, IndexError):
            pass
    raise ValueError(f'Unable to parse time string: {string}')