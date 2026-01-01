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
    try:
        from dateutil import parser
        return parser.parse(normalized)
    except ImportError:
        parts = normalized.split()
        date_part = parts[0]
        time_part = parts[1] if len(parts) > 1 else '00:00:00'
        date_part = date_part.replace('/', '-')
        date_formats = ['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y']
        for fmt in date_formats:
            try:
                date_obj = datetime.datetime.strptime(date_part, fmt).date()
                break
            except ValueError:
                continue
        else:
            raise ValueError(f'Unable to parse date: {date_part}')
        time_formats = ['%H:%M:%S', '%H:%M']
        for fmt in time_formats:
            try:
                time_obj = datetime.datetime.strptime(time_part, fmt).time()
                break
            except ValueError:
                continue
        else:
            time_obj = datetime.time(0, 0, 0)
        return datetime.datetime.combine(date_obj, time_obj)