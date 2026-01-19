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
            arg_type = self.types[arg]
            if arg_type == int:
                return int(value)
            elif arg_type == float:
                return float(value)
            elif arg_type == bool:
                if value.lower() in ('true', 't', 'yes', 'y', '1'):
                    return True
                elif value.lower() in ('false', 'f', 'no', 'n', '0'):
                    return False
                else:
                    return bool(value)
            elif arg_type == str:
                return str(value)
            else:
                return arg_type(value)
        except (ValueError, TypeError):
            return value
    return value