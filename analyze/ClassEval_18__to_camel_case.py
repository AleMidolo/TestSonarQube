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
    components = key.split('_')
    return components[0] + ''.join((x.title() for x in components[1:]))