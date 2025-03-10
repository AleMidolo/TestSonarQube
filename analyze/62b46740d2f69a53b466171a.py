def pretty(self, indent=0, debug=False):
    """
    Devuelve una representación formateada de manera legible de 'self'.
    """
    if debug:
        print(f"Debug: Indent level = {indent}")
    
    # Example implementation for a class with attributes
    if hasattr(self, '__dict__'):
        result = []
        for key, value in self.__dict__.items():
            if hasattr(value, 'pretty'):
                formatted_value = value.pretty(indent + 4, debug)
            else:
                formatted_value = repr(value)
            result.append(f"{' ' * indent}{key}: {formatted_value}")
        return "\n".join(result)
    else:
        return repr(self)