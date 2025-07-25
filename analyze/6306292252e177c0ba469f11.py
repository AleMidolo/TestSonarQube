def format_dt(dt):
    """
    使用 `ensure_timezone` 函数格式化 `dt` 的时间并返回时间。

    以 D* 节点期望的方式格式化日期时间。
    """
    if dt is None:
        return None
        
    # 确保时区信息存在
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
        
    # 转换为ISO格式字符串,去掉毫秒
    formatted = dt.isoformat()
    if '.' in formatted:
        formatted = formatted[:formatted.index('.')]
        
    # 添加Z表示UTC时区
    if formatted.endswith('+00:00'):
        formatted = formatted[:-6] + 'Z'
        
    return formatted