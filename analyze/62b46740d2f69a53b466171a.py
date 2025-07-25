def pretty(self, indent=0, debug=False):
    """
    स्वयं का एक सुंदर स्वरूपित प्रतिनिधित्व लौटाएँ।
    """
    indent_str = ' ' * indent
    result = f"{indent_str}{self.__class__.__name__}(\n"
    
    for key, value in self.__dict__.items():
        if debug:
            result += f"{indent_str}  {key}: {repr(value)}\n"
        else:
            result += f"{indent_str}  {key}: {value}\n"
    
    result += f"{indent_str})"
    return result