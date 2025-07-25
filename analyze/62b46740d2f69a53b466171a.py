def pretty(self, indent=0, debug=False):
    """
    स्वयं का एक सुंदर स्वरूपित प्रतिनिधित्व लौटाएँ।
    """
    indent_str = ' ' * indent
    result = f"{indent_str}{self.__class__.__name__}(\n"
    
    for key, value in self.__dict__.items():
        if debug:
            result += f"{indent_str}  {key}: {value}\n"
        else:
            if isinstance(value, (int, float, str, bool)):
                result += f"{indent_str}  {key}: {value}\n"
            elif isinstance(value, list):
                result += f"{indent_str}  {key}: [\n"
                for item in value:
                    if hasattr(item, 'pretty'):
                        result += item.pretty(indent + 4, debug)
                    else:
                        result += f"{indent_str}    {item}\n"
                result += f"{indent_str}  ]\n"
            elif hasattr(value, 'pretty'):
                result += f"{indent_str}  {key}: {value.pretty(indent + 4, debug)}\n"
            else:
                result += f"{indent_str}  {key}: {value}\n"
    
    result += f"{indent_str})"
    return result