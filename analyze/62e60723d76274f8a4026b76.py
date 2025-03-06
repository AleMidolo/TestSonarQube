from datetime import time, timedelta

class Time:
    def __init__(self, hour, minute, second, microsecond, tzinfo=None):
        self._time = time(hour, minute, second, microsecond, tzinfo)

    @classmethod
    def from_ticks(cls, ticks, tz=None):
        """
        Crea un'istanza di tempo a partire dai ticks (nanosecondi trascorsi dalla mezzanotte).

        :param ticks: nanosecondi trascorsi dalla mezzanotte
        :type ticks: int
        :param tz: fuso orario opzionale
        :type tz: datetime.tzinfo

        :rtype: Time

        :raises ValueError: se il valore di ticks è fuori dai limiti
            (0 <= ticks < 86400000000000)
        """
        if not (0 <= ticks < 86400000000000):
            raise ValueError("ticks must be in the range 0 <= ticks < 86400000000000")
        
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