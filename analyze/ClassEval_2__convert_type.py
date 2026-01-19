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
    if arg in self.types:
        try:
            if self.types[arg] == int:
                return int(value)
            elif self.types[arg] == float:
                return float(value)
            elif self.types[arg] == bool:
                if value.lower() in ('true', '1', 'yes'):
                    return True
                elif value.lower() in ('false', '0', 'no'):
                    return False
                else:
                    return bool(value)
            elif self.types[arg] == str:
                return str(value)
            else:
                return value
        except (ValueError, TypeError):
            return value
    return value