def string_to_datetime(self, string):
    """
        Convert the time string to a datetime instance
        :param string: string, string before converting format
        :return: datetime instance
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    formats_to_try = ['%Y-%m-%d %H:%M:%S', '%Y/%m/%d %H:%M:%S', '%Y.%m.%d %H:%M:%S', '%Y-%m-%d %H:%M', '%Y/%m/%d %H:%M', '%Y.%m.%d %H:%M', '%Y-%m-%d', '%Y/%m/%d', '%Y.%m.%d', '%Y-%m-%d %H:%M:%S.%f']
    for fmt in formats_to_try:
        try:
            return datetime.datetime.strptime(string, fmt)
        except ValueError:
            continue
    import re
    pattern = '\\b(\\d{1})\\b'

    def pad_single_digit(match):
        return f'0{match.group(1)}'
    padded_string = re.sub(pattern, pad_single_digit, string)
    for fmt in formats_to_try:
        try:
            return datetime.datetime.strptime(padded_string, fmt)
        except ValueError:
            continue
    raise ValueError(f'Unable to parse time string: {string}')