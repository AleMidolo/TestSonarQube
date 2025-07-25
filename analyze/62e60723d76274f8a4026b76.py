from datetime import datetime, time, timedelta

class Time:
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
        
        # Convert ticks to seconds and nanoseconds
        seconds = ticks // 1_000_000_000
        nanoseconds = ticks % 1_000_000_000
        
        # Create a datetime object at midnight
        midnight = datetime(1970, 1, 1)
        
        # Add the seconds and nanoseconds to midnight
        dt = midnight + timedelta(seconds=seconds, microseconds=nanoseconds // 1000)
        
        # Extract the time part
        t = dt.time()
        
        # If a timezone is provided, localize the time
        if tz is not None:
            dt = datetime.combine(dt.date(), t, tzinfo=tz)
            t = dt.timetz()
        
        return t