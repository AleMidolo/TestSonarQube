def status_str(self, prefix=''):
    """
    返回带有 self.log.status_str 的字符串表示形式，可选添加前缀。
    返回验证日志的字符串表示形式，可选添加前缀。
    """
    if hasattr(self, 'log') and hasattr(self.log, 'status_str'):
        status = self.log.status_str
    else:
        status = ''
        
    if prefix:
        return f"{prefix}{status}"
    return status