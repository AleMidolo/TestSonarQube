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
        
        # Create a timedelta from the microseconds
        delta = datetime.timedelta(microseconds=microseconds)
        
        # Create a datetime object at midnight and add the timedelta
        midnight = datetime.datetime(1, 1, 1, tzinfo=tz)
        dt = midnight + delta
        
        # Extract time components
        hour = dt.hour
        minute = dt.minute
        second = dt.second
        microsecond = dt.microsecond
        
        return cls(hour, minute, second, microsecond, tzinfo=tz)