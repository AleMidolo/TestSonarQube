@staticmethod
def _to_camel_case(key):
    """
        कुंजी स्ट्रिंग को कैमेल केस में परिवर्तित करें
        :param key:str
        :return:str, परिवर्तित कुंजी स्ट्रिंग
        >>> camelize_map = CamelCaseMap()
        >>> camelize_map._to_camel_case('first_name')
        'firstName'
        """
    if not key or '_' not in key:
        return key
    parts = key.split('_')
    return parts[0] + ''.join((part.capitalize() for part in parts[1:]))