from datetime import datetime, timedelta, timezone

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
            raise ValueError("ticks must be in the range 0 <= ticks < 86400000000000")
        
        # Convert ticks to microseconds
        microseconds = ticks // 1000
        
        # Create a timedelta from the microseconds
        delta = timedelta(microseconds=microseconds)
        
        # Create a datetime object at midnight and add the timedelta
        midnight = datetime(1, 1, 1, tzinfo=tz)
        dt = midnight + delta
        
        # Extract time components
        hour = dt.hour
        minute = dt.minute
        second = dt.second
        microsecond = dt.microsecond
        
        return cls(hour, minute, second, microsecond, tz)