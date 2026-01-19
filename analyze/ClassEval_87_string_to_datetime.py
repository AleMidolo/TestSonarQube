def string_to_datetime(self, string):
    """
        Converte la stringa di tempo in un'istanza di datetime
        :param string: stringa, stringa prima della conversione del formato
        :return: istanza di datetime
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats_to_try = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%Y.%m.%d %H:%M:%S', '%Y.%m.%d %H:%M', '%Y.%m.%d', '%d.%m.%Y %H:%M:%S', '%d.%m.%Y %H:%M', '%d.%m.%Y']
    for fmt in formats_to_try:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    normalized = string.replace('/', '-').replace('.', '-')
    parts = normalized.split()
    if len(parts) == 1:
        date_parts = parts[0].split('-')
        if len(date_parts) == 3:
            year, month, day = map(int, date_parts)
            return datetime.datetime(year, month, day)
    elif len(parts) == 2:
        date_parts = parts[0].split('-')
        time_parts = parts[1].split(':')
        if len(date_parts) == 3 and len(time_parts) >= 1:
            year, month, day = map(int, date_parts)
            hour = int(time_parts[0])
            minute = int(time_parts[1]) if len(time_parts) > 1 else 0
            second = int(time_parts[2]) if len(time_parts) > 2 else 0
            return datetime.datetime(year, month, day, hour, minute, second)
    raise ValueError(f'Unable to parse time string: {string}')