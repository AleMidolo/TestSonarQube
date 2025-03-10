from datetime import time, timedelta

class Time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=None):
        self._time = time(hour, minute, second, microsecond, tzinfo)

    @classmethod
    def from_ticks(cls, ticks, tz=None):
        """
        根据时间戳（自午夜以来的纳秒数）创建一个时间对象。

        :param ticks: 自午夜以来的纳秒数
        :type ticks: int
        :param tz: 可选的时区信息
        :type tz: datetime.tzinfo
        :rtype: Time
        :raises ValueError: 如果时间戳超出范围(0 <= ticks < 86400000000000)
        """
        if not (0 <= ticks < 86400000000000):
            raise ValueError("时间戳超出范围(0 <= ticks < 86400000000000)")
        
        # Convert ticks to microseconds
        microseconds = ticks // 1000
        
        # Calculate hours, minutes, seconds, and microseconds
        hours = microseconds // 3600000000
        microseconds %= 3600000000
        minutes = microseconds // 60000000
        microseconds %= 60000000
        seconds = microseconds // 1000000
        microseconds %= 1000000
        
        return cls(hours, minutes, seconds, microseconds, tz)