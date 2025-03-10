from datetime import time, timedelta

class Time(time):
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
            raise ValueError("Los ticks deben estar en el rango [0, 86400000000000)")
        
        nanoseconds = ticks % 1000
        microseconds = (ticks // 1000) % 1000
        milliseconds = (ticks // 1000000) % 1000
        seconds = (ticks // 1000000000) % 60
        minutes = (ticks // 60000000000) % 60
        hours = (ticks // 3600000000000) % 24
        
        return cls(hours, minutes, seconds, milliseconds * 1000 + microseconds, tzinfo=tz)