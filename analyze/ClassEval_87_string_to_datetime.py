def string_to_datetime(self, string):
    """
        Convierte la cadena de tiempo a una instancia de datetime
        :param string: string, cadena antes de convertir el formato
        :return: instancia de datetime
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y']
    for fmt in formats:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    normalized = string.strip()
    while '  ' in normalized:
        normalized = normalized.replace('  ', ' ')
    try:
        from dateutil import parser
        return parser.parse(normalized)
    except ImportError:
        parts = normalized.split(' ')
        date_part = parts[0]
        time_part = parts[1] if len(parts) > 1 else '00:00:00'
        for sep in ['-', '/', '.']:
            date_part = date_part.replace(sep, '-')
        time_part = time_part.replace(':', '-')
        date_parts = date_part.split('-')
        if len(date_parts) == 3:
            year, month, day = date_parts
            year = int(year)
            month = int(month)
            day = int(day)
        else:
            raise ValueError(f'Unable to parse date from: {string}')
        time_parts = time_part.split('-')
        if len(time_parts) == 3:
            hour, minute, second = time_parts
            hour = int(hour)
            minute = int(minute)
            second = int(second)
        elif len(time_parts) == 2:
            hour, minute = time_parts
            hour = int(hour)
            minute = int(minute)
            second = 0
        elif len(time_parts) == 1 and time_parts[0]:
            hour = int(time_parts[0])
            minute = 0
            second = 0
        else:
            hour = minute = second = 0
        return datetime.datetime(year, month, day, hour, minute, second)