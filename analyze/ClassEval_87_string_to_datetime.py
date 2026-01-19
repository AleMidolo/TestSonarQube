def string_to_datetime(self, string):
    """
        Converte la stringa di tempo in un'istanza di datetime
        :param string: stringa, stringa prima della conversione del formato
        :return: istanza di datetime
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
        try:
            parts = normalized.split(' ')
            date_part = parts[0]
            time_part = parts[1] if len(parts) > 1 else '0:0:0'
            date_parts = date_part.replace('-', '/').replace('.', '/').split('/')
            if len(date_parts) == 3:
                year = int(date_parts[0]) if len(date_parts[0]) == 4 else int(date_parts[2])
                month = int(date_parts[1])
                day = int(date_parts[0]) if len(date_parts[0]) != 4 else int(date_parts[2])
            time_parts = time_part.split(':')
            hour = int(time_parts[0]) if len(time_parts) > 0 else 0
            minute = int(time_parts[1]) if len(time_parts) > 1 else 0
            second = int(time_parts[2]) if len(time_parts) > 2 else 0
            return datetime.datetime(year, month, day, hour, minute, second)
        except:
            raise ValueError(f'Unable to parse time string: {string}')