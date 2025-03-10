from datetime import datetime, timezone

def ensure_timezone(dt):
    """
    确保给定的 datetime 对象具有时区信息。
    如果 dt 没有时区信息，则默认设置为 UTC。
    """
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt

def format_dt(dt):
    """
    使用 `ensure_timezone` 函数格式化 `dt` 的时间并返回时间。

    以 D* 节点期望的方式格式化日期时间。
    """
    dt_with_tz = ensure_timezone(dt)
    return dt_with_tz.isoformat()