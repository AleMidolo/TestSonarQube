def pretty(self, indent=0, debug=False):
    """
    返回对象自身的美观格式化表示。
    `obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj) return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"`
    """
    obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
    debug_details = f"DEBUG: {self.debug_info()}" if debug else ""
    return (" " * indent) + f"{self.__class__.__name__}({debug_details}{obj})"