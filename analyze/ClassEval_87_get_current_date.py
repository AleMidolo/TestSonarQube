def get_current_date(self):
    """
    返回当前日期,格式为 "%Y-%m-%d"
    :return: 字符串
    >>> timeutils.get_current_date()
    "2023-06-14"
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d")