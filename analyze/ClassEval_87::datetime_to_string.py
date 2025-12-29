def datetime_to_string(self, datetime):
    """
        एक datetime उदाहरण को एक स्ट्रिंग में परिवर्तित करें
        :param datetime: परिवर्तित करने के लिए datetime उदाहरण
        :return: स्ट्रिंग, परिवर्तित समय स्ट्रिंग
        >>> timeutils.datetime_to_string(timeutils.datetime)
        "2023-06-14 19:30:03"
        """
    format = '%Y-%m-%d %H:%M:%S'
    return datetime.strftime(format)