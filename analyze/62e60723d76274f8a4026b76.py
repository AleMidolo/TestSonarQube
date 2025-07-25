from datetime import time, timedelta

class Time:
    @classmethod
    def from_ticks(cls, ticks, tz=None):
        """
        Create a time from ticks (nanoseconds since midnight).

        :param ticks: nanoseconds since midnight
        :type ticks: int
        :param tz: optional timezone
        :type tz: datetime.tzinfo

        :rtype: Time

        :raises ValueError: if ticks is out of bounds
            (0 <= ticks < 86400000000000)
        """
        if not (0 <= ticks < 86400000000000):
            raise ValueError("ticks must be between 0 and 86400000000000 nanoseconds")
        
        # Convert ticks to seconds and microseconds
        seconds, nanoseconds = divmod(ticks, 1_000_000_000)
        microseconds = nanoseconds // 1_000
        
        # Create a timedelta representing the time since midnight
        delta = timedelta(seconds=seconds, microseconds=microseconds)
        
        # Create a time object from the timedelta
        midnight = time(0, 0, 0)
        time_obj = (datetime.combine(datetime.min, midnight) + delta).time()
        
        return time_obj