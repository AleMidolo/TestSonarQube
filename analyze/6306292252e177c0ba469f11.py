from datetime import datetime
import pytz

def ensure_timezone(dt):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=pytz.UTC)
    return dt.astimezone(pytz.UTC)

def format_dt(dt):
    """
    使用 `ensure_timezone` 函数格式化 `dt` 的时间并返回时间。

    以 D* 节点期望的方式格式化日期时间。
    """
    dt_with_tz = ensure_timezone(dt)
    return dt_with_tz.strftime('%Y-%m-%d %H:%M:%S %Z')