def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    indent_str = ' ' * indent
    representation = f"{indent_str}Class: {self.__class__.__name__}\n"
    
    if debug:
        representation += f"{indent_str}Debug Info: {vars(self)}\n"
    
    for attr, value in vars(self).items():
        representation += f"{indent_str}{attr}: {value}\n"
    
    return representation