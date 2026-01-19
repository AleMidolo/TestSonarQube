def string_to_datetime(self, string):
    """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats_to_try = ['%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y/%m/%d %H:%M', '%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d/%m/%Y %H:%M:%S', '%m-%d-%Y %H:%M:%S', '%m/%d/%Y %H:%M:%S']
    for fmt in formats_to_try:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    normalized_string = string.replace('/', '-').replace('.', '-')
    parts = normalized_string.split()
    date_part = parts[0]
    time_part = parts[1] if len(parts) > 1 else '00:00:00'
    date_parts = date_part.split('-')
    if len(date_parts) == 3:
        year, month, day = date_parts
        if len(year) == 2:
            year = '20' + year if int(year) < 50 else '19' + year
    else:
        raise ValueError(f'Unable to parse date from string: {string}')
    time_parts = time_part.split(':')
    if len(time_parts) == 3:
        hour, minute, second = time_parts
    elif len(time_parts) == 2:
        hour, minute = time_parts
        second = '00'
    else:
        hour, minute, second = ('00', '00', '00')
    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))