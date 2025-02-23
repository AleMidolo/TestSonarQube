def pretty(self, indent=0, debug=False):
    """
    Restituisce una rappresentazione formattata in modo leggibile di sé stesso.
    
    obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
    debug_details = "debug=True, " if debug else ""
    return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"