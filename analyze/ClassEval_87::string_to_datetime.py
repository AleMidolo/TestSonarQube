def string_to_datetime(self, string):
    """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats_to_try = ['%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y/%m/%d %H:%M', '%Y-%m-%d', '%Y/%m/%d', '%Y-%m-%d %H:%M:%S.%f']
    for fmt in formats_to_try:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    normalized = string.replace('/', '-').replace('.', '-')
    parts = normalized.split()
    date_part = parts[0]
    time_part = parts[1] if len(parts) > 1 else '00:00:00'
    date_parts = date_part.split('-')
    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])
    time_parts = time_part.split(':')
    hour = int(time_parts[0])
    minute = int(time_parts[1]) if len(time_parts) > 1 else 0
    second = int(time_parts[2]) if len(time_parts) > 2 else 0
    return datetime.datetime(year, month, day, hour, minute, second)