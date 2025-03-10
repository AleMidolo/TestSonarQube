import datetime

class Time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=None):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.microsecond = microsecond
        self.tzinfo = tzinfo

    @classmethod
    def from_ticks(cls, ticks, tz=None):
        """
        टिक से समय बनाएं (आधी रात के बाद से नैनोसेकंड)।

        :param ticks: आधी रात के बाद से नैनोसेकंड
        :type ticks: int
        :param tz: वैकल्पिक टाइमज़ोन
        :type tz: datetime.tzinfo

        :rtype: Time

        :raises ValueError: यदि ticks सीमा से बाहर है
            (0 <= ticks < 86400000000000)
        """
        if not (0 <= ticks < 86400000000000):
            raise ValueError("ticks must be in the range [0, 86400000000000)")

        nanoseconds_per_second = 1_000_000_000
        seconds = ticks // nanoseconds_per_second
        nanoseconds = ticks % nanoseconds_per_second

        microseconds = nanoseconds // 1000

        time = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=seconds)
        time = time.replace(microsecond=microseconds)

        if tz is not None:
            time = time.replace(tzinfo=tz)

        return cls(time.hour, time.minute, time.second, time.microsecond, tzinfo=tz)