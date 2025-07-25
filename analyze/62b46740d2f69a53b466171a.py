def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    if debug:
        print(f"Debug: Indent level = {indent}")
    
    # Assuming self is a dictionary-like object for this example
    if isinstance(self, dict):
        result = "{\n"
        for key, value in self.items():
            result += " " * (indent + 4) + f"{key}: "
            if isinstance(value, dict):
                result += value.pretty(indent + 4, debug) if hasattr(value, 'pretty') else str(value)
            else:
                result += str(value)
            result += ",\n"
        result = result.rstrip(",\n") + "\n" + " " * indent + "}"
        return result
    else:
        return str(self)