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
        Analizza la stringa di argomenti della riga di comando fornita e invoca _convert_type per memorizzare il risultato analizzato in un tipo specifico nel dizionario degli argomenti.
        Controlla la presenza di argomenti richiesti mancanti, se presenti, e restituisce False con i nomi degli argomenti mancanti, altrimenti restituisce True.
        :param command_string: str, stringa di argomenti della riga di comando, formattata come "python script.py --arg1=value1 -arg2 value2 --option1 -option2"
        :return tuple: (True, None) se l'analisi ha successo, (False, missing_args) se l'analisi fallisce,
            dove missing_args è un insieme dei nomi degli argomenti mancanti che sono str.
        >>> parser.parse_arguments("python script.py --arg1=value1 -arg2 value2 --option1 -option2")
        (True, None)
        >>> parser.arguments
        {'arg1': 'value1', 'arg2': 'value2', 'option1': True, 'option2': True}
        """
        import re
        
        # Split the command string into parts
        parts = re.split(r'\s+', command_string)
        # Remove the script name
        parts = parts[2:]  # Assuming the first two parts are 'python' and 'script.py'
        
        missing_args = set()
        
        for part in parts:
            if '=' in part:
                key, value = part.split('=', 1)
            else:
                key = part
                value = True  # Default value for flags
            
            # Normalize the key
            key = key.lstrip('-')
            
            # Convert the type if necessary
            if key in self.types:
                value = self._convert_type(key, value)
            
            self.arguments[key] = value
        
        # Check for missing required arguments
        missing_args = self.required - self.arguments.keys()
        
        if missing_args:
            return (False, missing_args)
        
        return (True, None)