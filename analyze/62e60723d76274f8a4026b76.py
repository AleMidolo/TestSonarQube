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
        Crear una hora a partir de ticks (nanosegundos desde la medianoche).

        :param ticks: nanosegundos desde la medianoche
        :type ticks: int
        :param tz: zona horaria opcional
        :type tz: datetime.tzinfo

        :rtype: Time

        :raises ValueError: si los ticks están fuera de los límites
            (0 <= ticks < 86400000000000)
        """
        if not (0 <= ticks < 86400000000000):
            raise ValueError("Ticks must be between 0 and 86400000000000")
        
        seconds, nanoseconds = divmod(ticks, 1_000_000_000)
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        microseconds = nanoseconds // 1000
        
        return cls(hours, minutes, seconds, microseconds, tz)