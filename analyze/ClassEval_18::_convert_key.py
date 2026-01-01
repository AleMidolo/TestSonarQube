def _convert_key(self, key):
    """
        कुंजी स्ट्रिंग को कैमेल केस में परिवर्तित करें
        :param key:str
        :return:str, परिवर्तित कुंजी स्ट्रिंग
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._convert_key('first_name')
        'firstName'
        """
    return self._to_camel_case(key)