def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    # Crear el string de indentación basado en el nivel
    indent_str = "  " * indent
    
    # Si debug está activado, incluir información adicional
    if debug:
        result = f"{indent_str}{self.__class__.__name__}("
    else:
        result = f"{indent_str}("
        
    # Obtener los atributos del objeto
    attrs = vars(self)
    
    # Formatear cada atributo
    formatted_attrs = []
    for key, value in attrs.items():
        # Si el valor tiene método pretty, usarlo recursivamente
        if hasattr(value, 'pretty'):
            attr_str = value.pretty(indent + 1, debug)
        else:
            attr_str = repr(value)
            
        if debug:
            formatted_attrs.append(f"{key}={attr_str}")
        else:
            formatted_attrs.append(attr_str)
            
    # Unir todos los atributos con comas
    result += ", ".join(formatted_attrs)
    result += ")"
    
    return result