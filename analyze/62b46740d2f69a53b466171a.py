def pretty(self, indent=0, debug=False):
    """
    返回对象自身的美观格式化表示。
    """
    # 处理对象值的表示形式
    obj = f"'{self.obj}'" if isinstance(self.obj, str) else repr(self.obj)
    
    # 如果开启debug模式，添加额外的调试信息
    debug_details = f"id={id(self)}, " if debug else ""
    
    # 构建缩进的格式化字符串
    indentation = " " * indent
    
    # 返回格式化后的字符串
    return indentation + f"{self.__class__.__name__}({debug_details}{obj})"