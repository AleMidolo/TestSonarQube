def string_to_datetime(self, string):
    """
        Converte la stringa di tempo in un'istanza di datetime
        :param string: stringa, stringa prima della conversione del formato
        :return: istanza di datetime
        >>> timeutils.string_to_datetime("2001-7-18 1:1:1")
        2001-07-18 01:01:01
        """
    try:
        return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            return datetime.datetime.strptime(string, '%Y-%m-%d %H:%M')
        except ValueError:
            try:
                return datetime.datetime.strptime(string, '%Y-%m-%d')
            except ValueError:
                try:
                    return datetime.datetime.strptime(string, '%Y/%m/%d %H:%M:%S')
                except ValueError:
                    try:
                        return datetime.datetime.strptime(string, '%Y/%m/%d %H:%M')
                    except ValueError:
                        try:
                            return datetime.datetime.strptime(string, '%Y/%m/%d')
                        except ValueError:
                            raise ValueError(f'Unable to parse time string: {string}')