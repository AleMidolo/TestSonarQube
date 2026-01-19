def _convert_key(self, key):
    """
    कुंजी स्ट्रिंग को कैमेल केस में परिवर्तित करें
    :param key:str
    :return:str, परिवर्तित कुंजी स्ट्रिंग
    >>> camelize_map = CamelCaseMap()
    >>> camelize_map._convert_key('first_name')
    'firstName'
    """
    parts = key.split('_')
    if len(parts) == 1:
        return key
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])