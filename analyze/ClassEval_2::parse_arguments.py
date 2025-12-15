class ArgumentParser: 
    def __init__(self):
        """
        Initialize the fields.
        self.arguments is a dict that stores the args in a command line
        self.requried is a set that stores the required arguments
        self.types is a dict that stores type of every arguments.
        >>> parser.arguments
        {'key1': 'value1', 'option1': True}
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'type1'}
        """
        self.arguments = {}
        self.required = set()
        self.types = {}

    def get_argument(self, key):
        """
        Retrieves the value of the specified argument from the arguments dictionary and returns it.
        :param key: str, argument name
        :return: The value of the argument, or None if the argument does not exist.
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        >>> parser.get_argument('arg2')
        'value2'
        """
        return self.arguments.get(key)
    
    def add_argument(self, arg, required=False, arg_type=str):
        """
        Adds an argument to self.types and self.required.
        Check if it is a required argument and store the argument type.
        If the argument is set as required, it wull be added to the required set.
        The argument type and name are stored in the types dictionary as key-value pairs.
        :param arg: str, argument name
        :param required: bool, whether the argument is required, default is False
        :param arg_type:str, Argument type, default is str
        >>> parser.add_argument('arg1', True, 'int')
        >>> parser.required
        {'arg1'}
        >>> parser.types
        {'arg1': 'int'}
        """
        if required:
            self.required.add(arg)
        self.types[arg] = arg_type
    
    def _convert_type(self, arg, value):
        """
        Try to convert the type of input value by searching in self.types.
        :param value: str, the input value in command line
        :return: return corresponding value in self.types if convert successfully, or the input value oherwise
        >>> parser.types
        {'arg1': int}
        >>> parser._convert_type('arg1', '21')
        21
        """
        try:
            return self.types[arg](value)
        except (ValueError, KeyError):
            return value
    
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
        
        # Split the command string into parts
        parts = re.split(r'\s+', command_string)
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
        
        # Check for missing required arguments
        missing_args = self.required - self.arguments.keys()
        if missing_args:
            return (False, missing_args)
        
        return (True, None)