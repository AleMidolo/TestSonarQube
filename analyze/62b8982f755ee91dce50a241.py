def normalized(self):
    # Initialize variables to store total values
    total_microseconds = 0
    total_seconds = 0
    total_minutes = 0
    total_hours = 0
    total_days = 0
    total_months = 0
    total_years = 0

    # Convert fractional values to whole numbers in smaller units
    if hasattr(self, 'microseconds'):
        total_microseconds = int(self.microseconds)
    if hasattr(self, 'seconds'):
        total_seconds = int(self.seconds)
        frac_seconds = self.seconds - total_seconds
        total_microseconds += int(frac_seconds * 1000000)
    if hasattr(self, 'minutes'):
        total_minutes = int(self.minutes)
        frac_minutes = self.minutes - total_minutes
        total_seconds += int(frac_minutes * 60)
    if hasattr(self, 'hours'):
        total_hours = int(self.hours)
        frac_hours = self.hours - total_hours
        total_minutes += int(frac_hours * 60)
    if hasattr(self, 'days'):
        total_days = int(self.days)
        frac_days = self.days - total_days
        total_hours += int(frac_days * 24)
    if hasattr(self, 'months'):
        total_months = int(self.months)
        frac_months = self.months - total_months
        total_days += int(frac_months * 30)  # Approximate
    if hasattr(self, 'years'):
        total_years = int(self.years)
        frac_years = self.years - total_years
        total_months += int(frac_years * 12)

    # Normalize smaller units into larger ones
    # Microseconds to seconds
    extra_seconds = total_microseconds // 1000000
    total_microseconds = total_microseconds % 1000000
    total_seconds += extra_seconds

    # Seconds to minutes
    extra_minutes = total_seconds // 60
    total_seconds = total_seconds % 60
    total_minutes += extra_minutes

    # Minutes to hours
    extra_hours = total_minutes // 60
    total_minutes = total_minutes % 60
    total_hours += extra_hours

    # Hours to days
    extra_days = total_hours // 24
    total_hours = total_hours % 24
    total_days += extra_days

    # Days to months (approximate)
    extra_months = total_days // 30
    total_days = total_days % 30
    total_months += extra_months

    # Months to years
    extra_years = total_months // 12
    total_months = total_months % 12
    total_years += extra_years

    # Return new relativedelta object with normalized values
    return type(self)(years=total_years,
                     months=total_months,
                     days=total_days,
                     hours=total_hours,
                     minutes=total_minutes,
                     seconds=total_seconds,
                     microseconds=total_microseconds)