def status_str(self, prefix=''):
    """
    返回带有 `self.log.status_str` 的字符串表示形式，可选添加前缀。
    返回验证日志的字符串表示形式，可选添加前缀。
    """
    return f"{prefix}{self.log.status_str()}"