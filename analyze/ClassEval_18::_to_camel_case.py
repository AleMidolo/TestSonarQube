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
    if not key:
        return key
    parts = key.split('_')
    result = parts[0].lower()
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:].lower()
    return result