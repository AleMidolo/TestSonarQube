def pretty(self, indent=0, debug=False):
    obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
    debug_details = f"{self.debug_info()}" if debug else ""
    return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"