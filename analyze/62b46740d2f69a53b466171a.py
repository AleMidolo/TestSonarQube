def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    if debug:
        print(f"Debug: Indent level = {indent}")
    
    # Asumiendo que self es un diccionario o una lista para este ejemplo
    if isinstance(self, dict):
        result = "{\n"
        for key, value in self.items():
            result += " " * (indent + 4) + f"{repr(key)}: "
            if isinstance(value, (dict, list)):
                result += value.pretty(indent + 4, debug)
            else:
                result += repr(value)
            result += ",\n"
        result += " " * indent + "}"
    elif isinstance(self, list):
        result = "[\n"
        for item in self:
            result += " " * (indent + 4)
            if isinstance(item, (dict, list)):
                result += item.pretty(indent + 4, debug)
            else:
                result += repr(item)
            result += ",\n"
        result += " " * indent + "]"
    else:
        result = repr(self)
    
    return result