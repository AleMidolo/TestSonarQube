def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    # Crear el string de indentación basado en el nivel de indent
    indent_str = "  " * indent
    
    # Si debug está activado, incluir información adicional
    if debug:
        result = f"{indent_str}{self.__class__.__name__}:\n"
    else:
        result = f"{indent_str}"

    # Si el objeto es una colección (lista, diccionario, etc)
    if hasattr(self, '__iter__') and not isinstance(self, (str, bytes)):
        # Para diccionarios
        if isinstance(self, dict):
            items = [f"{indent_str}  {k}: {v.pretty(indent+1) if hasattr(v, 'pretty') else v}" 
                    for k, v in self.items()]
            result += "{\n" + ",\n".join(items) + f"\n{indent_str}}}"
        
        # Para listas, tuplas, sets
        else:
            items = [f"{indent_str}  {item.pretty(indent+1) if hasattr(item, 'pretty') else item}" 
                    for item in self]
            result += "[\n" + ",\n".join(items) + f"\n{indent_str}]"
    
    # Para objetos simples
    else:
        result += str(self)
    
    return result