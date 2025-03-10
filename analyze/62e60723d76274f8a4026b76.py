import datetime

class Time:
    def __init__(self, nanoseconds):
        self.nanoseconds = nanoseconds

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
            raise ValueError("ticks must be in the range 0 <= ticks < 86400000000000")
        
        nanoseconds = ticks
        return cls(nanoseconds)