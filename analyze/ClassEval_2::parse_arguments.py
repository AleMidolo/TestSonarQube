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
    import re
    parts = re.split('\\s+', command_string)
    for part in parts:
        if '=' in part:
            key, value = part.split('=', 1)
            key = key.lstrip('-')
            self.arguments[key] = self._convert_type(key, value)
        elif part.startswith('-'):
            key = part.lstrip('-')
            self.arguments[key] = True
        else:
            continue
    missing_args = self.required - self.arguments.keys()
    if missing_args:
        return (False, missing_args)
    return (True, None)