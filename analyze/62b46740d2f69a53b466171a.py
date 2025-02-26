def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    indent_str = ' ' * indent
    representation = f"{indent_str}Class: {self.__class__.__name__}\n"
    
    for attr, value in self.__dict__.items():
        representation += f"{indent_str}  {attr}: {value}\n"
    
    if debug:
        representation += f"{indent_str}  Debug Info: {self.__dict__}\n"
    
    return representation