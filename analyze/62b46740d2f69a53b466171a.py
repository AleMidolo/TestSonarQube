def pretty(self, indent=0, debug=False):
    """
    स्वयं का एक सुंदर स्वरूपित प्रतिनिधित्व लौटाएँ।
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
    
    # Build the string representation
    if attrs:
        result += "\n"
        for attr in attrs:
            value = getattr(self, attr)
            # Handle nested objects that may have pretty() method
            if hasattr(value, 'pretty'):
                attr_str = value.pretty(indent + 2, debug)
            else:
                attr_str = repr(value)
            result += f"{indent_str}  {attr}={attr_str},\n"
        result += indent_str
    
    result += ")"
    return result