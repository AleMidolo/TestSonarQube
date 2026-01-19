def get_current_time(self):
    """
    返回当前时间，格式为 '%H:%M:%S'
    :return: 字符串
    >>> timeutils = TimeUtils()
    >>> timeutils.get_current_time()
    "19:19:22"
    """
    return datetime.now().strftime('%H:%M:%S')