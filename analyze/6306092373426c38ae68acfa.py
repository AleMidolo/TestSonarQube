def get_spec_defaults(self):
    """
    使用 `self._get_defaults()` 从规范和其他来源解析参数的值。

    从规范和其他来源解析参数的值。
    """
    # 调用内部方法获取默认值
    defaults = self._get_defaults()
    
    # 如果有规范定义,从规范中获取默认值
    if hasattr(self, 'spec'):
        spec_defaults = getattr(self.spec, 'defaults', {})
        defaults.update(spec_defaults)
    
    # 从其他来源获取默认值
    other_defaults = {}
    
    # 如果有配置文件,从配置文件读取默认值
    if hasattr(self, 'config'):
        other_defaults.update(self.config.get('defaults', {}))
        
    # 如果有环境变量,从环境变量读取默认值
    if hasattr(self, 'env'):
        other_defaults.update(self.env.get_defaults())
    
    # 合并所有默认值
    defaults.update(other_defaults)
    
    return defaults