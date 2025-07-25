def get_spec_defaults(self):
    """
    使用 `self._get_defaults()` 从规范和其他来源解析参数的值。

    从规范和其他来源解析参数的值。
    """
    # 调用内部方法获取默认值
    defaults = self._get_defaults()
    
    # 如果规范中定义了默认值,则更新defaults
    if hasattr(self, 'spec') and self.spec is not None:
        spec_defaults = getattr(self.spec, 'defaults', {})
        defaults.update(spec_defaults)
        
    # 如果有其他来源的默认值,继续更新defaults
    if hasattr(self, 'other_defaults') and self.other_defaults is not None:
        defaults.update(self.other_defaults)
        
    return defaults