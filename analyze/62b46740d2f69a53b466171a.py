def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    if debug:
        print(f"Debug: Indent level = {indent}")
    
    # Assuming self is a dictionary or a list for this example
    if isinstance(self, dict):
        result = "{\n"
        for key, value in self.items():
            result += " " * (indent + 4) + f"{repr(key)}: "
            if isinstance(value, (dict, list)):
                result += value.pretty(indent + 4, debug) + ",\n"
            else:
                result += repr(value) + ",\n"
        result += " " * indent + "}"
    elif isinstance(self, list):
        result = "[\n"
        for item in self:
            if isinstance(item, (dict, list)):
                result += " " * (indent + 4) + item.pretty(indent + 4, debug) + ",\n"
            else:
                result += " " * (indent + 4) + repr(item) + ",\n"
        result += " " * indent + "]"
    else:
        result = repr(self)
    
    return result