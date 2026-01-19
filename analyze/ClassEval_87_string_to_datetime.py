def string_to_datetime(self, string):
    """
        Converte la stringa di tempo in un'istanza di datetime
        :param string: stringa, stringa prima della conversione del formato
        :return: istanza di datetime
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%Y.%m.%d %H:%M:%S', '%Y.%m.%d %H:%M', '%Y.%m.%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%d.%m.%Y %H:%M:%S', '%d.%m.%Y %H:%M', '%d.%m.%Y']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    import re
    normalized = re.sub('[/.-]', '-', string)
    date_time_parts = normalized.split()
    date_part = date_time_parts[0]
    time_part = date_time_parts[1] if len(date_time_parts) > 1 else '00:00:00'
    date_components = date_part.split('-')
    if len(date_components) == 3:
        year, month, day = date_components
        if len(year) == 2:
            year = '20' + year if int(year) < 50 else '19' + year
    else:
        raise ValueError(f'Unable to parse date from string: {string}')
    time_components = time_part.split(':')
    if len(time_components) == 3:
        hour, minute, second = time_components
    elif len(time_components) == 2:
        hour, minute = time_components
        second = '00'
    else:
        hour, minute, second = ('00', '00', '00')
    return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))