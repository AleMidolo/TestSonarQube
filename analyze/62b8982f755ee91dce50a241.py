def normalized(self):
    # Initialize variables to store total values
    total_microseconds = 0
    total_seconds = 0
    total_minutes = 0
    total_hours = 0
    total_days = 0
    total_months = 0
    total_years = 0

    # Convert fractional values to whole numbers
    if hasattr(self, 'microseconds'):
        total_microseconds = int(self.microseconds)
    if hasattr(self, 'seconds'): 
        total_seconds = int(self.seconds)
    if hasattr(self, 'minutes'):
        total_minutes = int(self.minutes) 
    if hasattr(self, 'hours'):
        total_hours = int(self.hours)
    if hasattr(self, 'days'):
        total_days = int(self.days)
    if hasattr(self, 'months'):
        total_months = int(self.months)
    if hasattr(self, 'years'):
        total_years = int(self.years)

    # Handle fractional parts
    if hasattr(self, 'microseconds'):
        frac_microseconds = self.microseconds - total_microseconds
        total_seconds += int(frac_microseconds * 1e-6)
        
    if hasattr(self, 'seconds'):
        frac_seconds = self.seconds - total_seconds
        total_minutes += int(frac_seconds / 60)
        
    if hasattr(self, 'minutes'):
        frac_minutes = self.minutes - total_minutes
        total_hours += int(frac_minutes / 60)
        
    if hasattr(self, 'hours'):
        frac_hours = self.hours - total_hours
        total_days += int(frac_hours / 24)
        
    if hasattr(self, 'days'):
        frac_days = self.days - total_days
        total_months += int(frac_days / 30)  # Approximate
        
    if hasattr(self, 'months'):
        frac_months = self.months - total_months
        total_years += int(frac_months / 12)

    # Normalize smaller units into larger ones
    if total_microseconds >= 1000000:
        total_seconds += total_microseconds // 1000000
        total_microseconds = total_microseconds % 1000000
        
    if total_seconds >= 60:
        total_minutes += total_seconds // 60
        total_seconds = total_seconds % 60
        
    if total_minutes >= 60:
        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60
        
    if total_hours >= 24:
        total_days += total_hours // 24
        total_hours = total_hours % 24
        
    if total_days >= 30:  # Approximate
        total_months += total_days // 30
        total_days = total_days % 30
        
    if total_months >= 12:
        total_years += total_months // 12
        total_months = total_months % 12

    # Create and return new relativedelta object
    from dateutil.relativedelta import relativedelta
    return relativedelta(
        years=total_years,
        months=total_months,
        days=total_days,
        hours=total_hours,
        minutes=total_minutes,
        seconds=total_seconds,
        microseconds=total_microseconds
    )