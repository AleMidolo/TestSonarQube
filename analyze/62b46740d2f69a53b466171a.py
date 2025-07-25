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
    
    # Build pretty string representation of attributes
    attr_strings = []
    for attr in attrs:
        value = getattr(self, attr)
        
        # Handle nested objects that may have pretty() method
        if hasattr(value, 'pretty'):
            attr_val = value.pretty(indent + 2, debug)
        else:
            attr_val = repr(value)
            
        attr_strings.append(f"{attr}={attr_val}")
    
    # Join attributes with commas and newlines
    if attr_strings:
        result += "\n"
        result += ",\n".join(f"{indent_str}  {s}" for s in attr_strings)
        result += "\n" + indent_str
        
    result += ")"
    
    # Add debug info if requested
    if debug:
        result += f" at {hex(id(self))}"
        
    return result