def normalized(self):
    # Convert all float values to integer values
    days = int(self.days)
    hours_remainder = (self.days - days) * 24 + self.hours
    hours = int(hours_remainder)
    minutes_remainder = (hours_remainder - hours) * 60 + self.minutes
    minutes = int(minutes_remainder)
    seconds_remainder = (minutes_remainder - minutes) * 60 + self.seconds
    seconds = int(seconds_remainder)
    microseconds = int((seconds_remainder - seconds) * 1000000 + self.microseconds)

    # Handle microseconds overflow
    if microseconds >= 1000000:
        seconds += microseconds // 1000000
        microseconds = microseconds % 1000000
    
    # Handle seconds overflow
    if seconds >= 60:
        minutes += seconds // 60
        seconds = seconds % 60

    # Handle minutes overflow
    if minutes >= 60:
        hours += minutes // 60
        minutes = minutes % 60

    # Handle hours overflow
    if hours >= 24:
        days += hours // 24
        hours = hours % 24

    return self.__class__(
        years=self.years,
        months=self.months,
        days=days,
        hours=hours,
        minutes=minutes,
        seconds=seconds,
        microseconds=microseconds,
        leapdays=self.leapdays,
        year=self.year,
        month=self.month,
        day=self.day,
        weekday=self.weekday,
    )