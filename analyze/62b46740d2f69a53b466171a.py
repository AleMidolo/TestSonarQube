def pretty(self, indent=0, debug=False):
    """
    Return a pretty formatted representation of self.
    """
    indent_str = ' ' * indent
    result = f"{indent_str}{self.__class__.__name__}(\n"
    
    for key, value in self.__dict__.items():
        if isinstance(value, (list, tuple)):
            result += f"{indent_str}    {key}: [\n"
            for item in value:
                if hasattr(item, 'pretty'):
                    result += item.pretty(indent + 8, debug) + ",\n"
                else:
                    result += f"{indent_str}        {repr(item)},\n"
            result += f"{indent_str}    ],\n"
        elif hasattr(value, 'pretty'):
            result += f"{indent_str}    {key}: {value.pretty(indent + 4, debug)},\n"
        else:
            result += f"{indent_str}    {key}: {repr(value)},\n"
    
    result += f"{indent_str})"
    return result