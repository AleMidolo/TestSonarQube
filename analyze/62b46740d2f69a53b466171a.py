def pretty(self, indent=0, debug=False):
    """
    स्वयं का एक सुंदर स्वरूपित प्रतिनिधित्व लौटाएँ।
    """
    representation = " " * indent + f"<{self.__class__.__name__}>\n"
    if debug:
        representation += " " * (indent + 2) + f"Debug Info: {self.__dict__}\n"
    return representation