from datetime import datetime
import pytz

def format_dt(dt):
    """
    使用 `ensure_timezone` 函数格式化 `dt` 的时间并返回时间。

    以 D* 节点期望的方式格式化日期时间。
    """
    def ensure_timezone(dt):
        if dt.tzinfo is None:
            return pytz.utc.localize(dt)
        return dt.astimezone(pytz.utc)

    dt_with_tz = ensure_timezone(dt)
    return dt_with_tz.strftime('%Y-%m-%dT%H:%M:%SZ')