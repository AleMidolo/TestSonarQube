def _convert_type(self, arg, value):
    """
    इनपुट मान के प्रकार को self.types में खोजकर परिवर्तित करने का प्रयास करें।
    :param value: str, कमांड लाइन में इनपुट मान
    :return: यदि सफलतापूर्वक परिवर्तित हो जाए तो self.types में संबंधित मान लौटाएं, अन्यथा इनपुट मान लौटाएं
    >>> parser.types
    {'arg1': int}
    >>> parser._convert_type('arg1', '21')
    21
    """
    if hasattr(self, 'types') and arg in self.types:
        try:
            return self.types[arg](value)
        except (ValueError, TypeError):
            return value
    return value