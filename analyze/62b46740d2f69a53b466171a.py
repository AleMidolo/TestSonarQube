def pretty(self, indent=0, debug=False):
    """
    स्वयं का एक सुंदर स्वरूपित प्रतिनिधित्व लौटाएँ।
    """
    # Create indentation string
    indent_str = " " * indent
    
    # Get the string representation of the object
    if debug:
        # Include more detailed debug information
        result = f"{indent_str}{self.__class__.__name__}:\n"
        for attr, value in self.__dict__.items():
            result += f"{indent_str}  {attr}: {value}\n"
        return result.rstrip()
    else:
        # Basic pretty formatting
        return f"{indent_str}{str(self)}"