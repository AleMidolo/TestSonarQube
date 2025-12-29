def string_to_datetime(self, string):
    """
        समय स्ट्रिंग को datetime उदाहरण में परिवर्तित करें
        :param string: स्ट्रिंग, प्रारूप परिवर्तित करने से पहले की स्ट्रिंग
        :return: datetime उदाहरण
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