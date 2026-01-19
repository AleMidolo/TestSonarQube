def add_seconds(self, seconds):
    """
    将指定的秒数添加到当前时间
    :param seconds: int, 要添加的秒数
    :return: string, 添加指定秒数后的时间，格式为 '%H:%M:%S'
    >>> timeutils.add_seconds(600)
    "19:29:22"
    """
    from datetime import datetime, timedelta
    
    current_time = datetime.now()
    new_time = current_time + timedelta(seconds=seconds)
    return new_time.strftime('%H:%M:%S')