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
    self.arguments = {}
    parts = command_string.split()
    i = 0
    while i < len(parts):
        part = parts[i]
        if part.startswith('--') and '=' in part:
            arg_name = part[2:].split('=')[0]
            arg_value = part.split('=', 1)[1]
            converted_value = self._convert_type(arg_name, arg_value)
            self.arguments[arg_name] = converted_value
            i += 1
        elif part.startswith('--'):
            arg_name = part[2:]
            if i + 1 < len(parts) and (not parts[i + 1].startswith('-')):
                arg_value = parts[i + 1]
                converted_value = self._convert_type(arg_name, arg_value)
                self.arguments[arg_name] = converted_value
                i += 2
            else:
                self.arguments[arg_name] = True
                i += 1
        elif part.startswith('-') and (not part.startswith('--')):
            arg_name = part[1:]
            if i + 1 < len(parts) and (not parts[i + 1].startswith('-')):
                arg_value = parts[i + 1]
                converted_value = self._convert_type(arg_name, arg_value)
                self.arguments[arg_name] = converted_value
                i += 2
            else:
                self.arguments[arg_name] = True
                i += 1
        else:
            i += 1
    missing_args = set()
    for req_arg in self.required:
        if req_arg not in self.arguments:
            missing_args.add(req_arg)
    if missing_args:
        return (False, missing_args)
    else:
        return (True, None)