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
            raise ValueError("ticks must be between 0 and 86400000000000")

        # Convert ticks to microseconds
        microseconds = ticks // 1000

        # Create a timedelta representing the time since midnight
        delta = timedelta(microseconds=microseconds)

        # Extract hours, minutes, seconds, and microseconds
        hours, remainder = divmod(delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        microseconds = delta.microseconds

        return cls(hours, minutes, seconds, microseconds, tz)