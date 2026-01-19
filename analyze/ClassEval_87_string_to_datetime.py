def string_to_datetime(self, string):
    """
        Convierte la cadena de tiempo a una instancia de datetime
        :param string: string, cadena antes de convertir el formato
        :return: instancia de datetime
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats = ['%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y-%m-%d', '%Y/%m/%d %H:%M:%S', '%Y/%m/%d %H:%M', '%Y/%m/%d', '%d-%m-%Y %H:%M:%S', '%d-%m-%Y %H:%M', '%d-%m-%Y', '%d/%m/%Y %H:%M:%S', '%d/%m/%Y %H:%M', '%d/%m/%Y', '%Y.%m.%d %H:%M:%S', '%Y.%m.%d %H:%M', '%Y.%m.%d', '%d.%m.%Y %H:%M:%S', '%d.%m.%Y %H:%M', '%d.%m.%Y']
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
            if len(date_parts[0]) == 4:
                year, month, day = date_parts
            else:
                day, month, year = date_parts
                if int(month) > 12 and int(day) <= 12:
                    month, day = (day, month)
        else:
            raise ValueError(f'Unable to parse date: {string}')
        time_parts = time_part.split(':')
        if len(time_parts) == 3:
            hour, minute, second = time_parts
        elif len(time_parts) == 2:
            hour, minute = time_parts
            second = 0
        else:
            hour, minute, second = (0, 0, 0)
        return datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))