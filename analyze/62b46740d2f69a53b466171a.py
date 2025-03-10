def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    if debug:
        print(f"Debug: Indent level = {indent}")
    
    # Assuming 'self' is a dictionary-like object for this example
    if isinstance(self, dict):
        result = "{\n"
        for key, value in self.items():
            result += " " * (indent + 4) + f"{repr(key)}: "
            if isinstance(value, dict):
                result += value.pretty(indent + 4, debug) if hasattr(value, 'pretty') else pretty(value, indent + 4, debug)
            else:
                result += repr(value)
            result += ",\n"
        result += " " * indent + "}"
        return result
    elif isinstance(self, list):
        result = "[\n"
        for item in self:
            result += " " * (indent + 4)
            if isinstance(item, dict):
                result += item.pretty(indent + 4, debug) if hasattr(item, 'pretty') else pretty(item, indent + 4, debug)
            else:
                result += repr(item)
            result += ",\n"
        result += " " * indent + "]"
        return result
    else:
        return repr(self)