def pretty(self, indent=0, debug=False):
    """
    Return a pretty formatted representation of self.
    """
    # Create indentation string based on indent level
    indent_str = " " * indent
    
    # Start with class name
    result = f"{indent_str}{self.__class__.__name__}("
    
    # Get all attributes that don't start with underscore
    attrs = [attr for attr in vars(self) if not attr.startswith('_')]
    
    # If in debug mode, include all attributes including private ones
    if debug:
        attrs = list(vars(self).keys())
    
    # Format each attribute
    formatted_attrs = []
    for attr in attrs:
        value = getattr(self, attr)
        # Handle nested objects that might have pretty() method
        if hasattr(value, 'pretty'):
            attr_str = value.pretty(indent + 2, debug)
        else:
            attr_str = repr(value)
        formatted_attrs.append(f"{attr}={attr_str}")
    
    # Join all formatted attributes
    if formatted_attrs:
        result += "\n"
        for attr in formatted_attrs[:-1]:
            result += f"{indent_str}  {attr},\n"
        result += f"{indent_str}  {formatted_attrs[-1]}\n"
        result += f"{indent_str})"
    else:
        result += ")"
        
    return result