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
    string = string.strip()
    parts = string.split(' ')
    if len(parts) == 2:
        date_part, time_part = parts
    elif len(parts) == 1:
        date_part = parts[0]
        time_part = '00:00:00'
    else:
        raise ValueError(f'Unable to parse time string: {string}')
    date_formats = ['%Y-%m-%d', '%Y/%m/%d', '%d-%m-%Y', '%d/%m/%Y', '%Y.%m.%d', '%d.%m.%Y']
    date_obj = None
    for fmt in date_formats:
        try:
            date_obj = datetime.datetime.strptime(date_part, fmt).date()
            break
        except ValueError:
            continue
    if date_obj is None:
        for sep in ['-', '/', '.']:
            if sep in date_part:
                date_components = date_part.split(sep)
                if len(date_components) == 3:
                    try:
                        year = int(date_components[0])
                        month = int(date_components[1])
                        day = int(date_components[2])
                        if year < 100:
                            year += 2000 if year < 50 else 1900
                        date_obj = datetime.date(year, month, day)
                        break
                    except (ValueError, IndexError):
                        continue
    if date_obj is None:
        raise ValueError(f'Unable to parse date part: {date_part}')
    time_formats = ['%H:%M:%S', '%H:%M']
    time_obj = None
    for fmt in time_formats:
        try:
            time_obj = datetime.datetime.strptime(time_part, fmt).time()
            break
        except ValueError:
            continue
    if time_obj is None:
        time_components = time_part.split(':')
        if len(time_components) >= 2:
            try:
                hour = int(time_components[0])
                minute = int(time_components[1])
                second = int(time_components[2]) if len(time_components) > 2 else 0
                time_obj = datetime.time(hour, minute, second)
            except (ValueError, IndexError):
                time_obj = datetime.time(0, 0, 0)
        else:
            time_obj = datetime.time(0, 0, 0)
    return datetime.datetime.combine(date_obj, time_obj)