def pretty(self, indent=0, debug=False):
    """
    स्वयं का एक सुंदर स्वरूपित प्रतिनिधित्व लौटाएँ।
    """
    # Create indentation string based on indent level
    indent_str = " " * indent
    
    # Start with class name
    result = f"{indent_str}{self.__class__.__name__}("
    
    # Get all attributes that don't start with underscore
    attrs = [attr for attr in dir(self) if not attr.startswith('_')]
    
    # Build the string representation
    attr_strings = []
    for attr in attrs:
        value = getattr(self, attr)
        # If debug mode is on, include more details
        if debug:
            attr_strings.append(f"{attr}={repr(value)}")
        else:
            # For non-debug mode, use str() for cleaner output
            attr_strings.append(f"{attr}={str(value)}")
    
    # Join all attributes with commas
    result += ", ".join(attr_strings)
    result += ")"
    
    return result