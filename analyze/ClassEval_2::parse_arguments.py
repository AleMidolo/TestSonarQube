def parse_arguments(self, command_string):
    """
        दिए गए कमांड लाइन तर्क स्ट्रिंग का विश्लेषण करता है और _convert_type को कॉल करता है ताकि विश्लेषित परिणाम को तर्कों की शब्दकोश में विशिष्ट प्रकार में संग्रहीत किया जा सके।
        यदि कोई आवश्यक तर्क गायब है, तो इसकी जांच करता है और गायब तर्क नामों के साथ False लौटाता है, अन्यथा True लौटाता है।
        :param command_string: str, कमांड लाइन तर्क स्ट्रिंग, इस तरह से स्वरूपित "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) यदि विश्लेषण सफल है, (False, missing_args) यदि विश्लेषण विफल होता है,
            जहाँ missing_args गायब तर्क नामों का एक सेट है जो str हैं।
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
    args = command_string.split()
    for arg in args[1:]:
        if '=' in arg:
            key, value = arg.split('=', 1)
        else:
            key = arg
            value = True
        key = key.lstrip('-')
        if key in self.types:
            self.arguments[key] = self._convert_type(key, value)
        else:
            self.arguments[key] = value
    missing_args = {arg for arg in self.required if arg not in self.arguments}
    return (len(missing_args) == 0, missing_args if missing_args else None)