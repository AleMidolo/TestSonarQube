def normalized(self):
    days = 0
    hours = 0
    minutes = 0
    seconds = 0
    microseconds = 0

    # Convert fractional days to hours
    if self.days:
        days = int(self.days)
        hours += (self.days - days) * 24

    # Convert fractional hours to minutes 
    if self.hours or hours:
        total_hours = self.hours + hours
        hours = int(total_hours)
        minutes += (total_hours - hours) * 60

    # Convert fractional minutes to seconds
    if self.minutes or minutes:
        total_minutes = self.minutes + minutes
        minutes = int(total_minutes)
        seconds += (total_minutes - minutes) * 60

    # Convert fractional seconds to microseconds
    if self.seconds or seconds:
        total_seconds = self.seconds + seconds
        seconds = int(total_seconds)
        microseconds += (total_seconds - seconds) * 1000000

    if self.microseconds or microseconds:
        total_microseconds = self.microseconds + microseconds
        microseconds = int(total_microseconds)

    # Create new relativedelta with normalized values
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
        hour=self.hour,
        minute=self.minute,
        second=self.second,
        microsecond=self.microsecond
    )