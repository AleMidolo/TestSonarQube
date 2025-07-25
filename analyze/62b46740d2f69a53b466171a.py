def pretty(self, indent=0, debug=False):
    """
    Return a pretty formatted representation of self.
    """
    indent_str = ' ' * indent
    result = f"{indent_str}{self.__class__.__name__}(\n"
    
    for key, value in self.__dict__.items():
        if debug:
            result += f"{indent_str}  {key}: {repr(value)}\n"
        else:
            if isinstance(value, (list, dict, set)):
                result += f"{indent_str}  {key}: {value}\n"
            else:
                result += f"{indent_str}  {key}: {value}\n"
    
    result += f"{indent_str})"
    return result