from dateutil.relativedelta import relativedelta

def normalized(self):
    """
    यह फ़ंक्शन इस ऑब्जेक्ट का एक ऐसा संस्करण लौटाता है, जिसमें सभी सापेक्ष गुण (relative attributes) पूरी तरह से पूर्णांक मानों (integer values) में दर्शाए गए हों।

    उदाहरण:

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :वापसी मान (Return):
    यह एक `dateutil.relativedelta.relativedelta` क्लास का ऑब्जेक्ट लौटाता है।
    """
    # Convert all relative attributes to integer values
    days = int(self.days)
    hours = int(self.hours)
    minutes = int(self.minutes)
    seconds = int(self.seconds)
    microseconds = int(self.microseconds)
    
    # Calculate the remaining fractional parts and add them to the next higher unit
    remaining_days = self.days - days
    remaining_hours = self.hours - hours
    remaining_minutes = self.minutes - minutes
    remaining_seconds = self.seconds - seconds
    remaining_microseconds = self.microseconds - microseconds
    
    # Add the remaining fractional parts to the next higher unit
    hours += int(remaining_days * 24)
    minutes += int(remaining_hours * 60)
    seconds += int(remaining_minutes * 60)
    microseconds += int(remaining_seconds * 1e6)
    
    # Normalize the values to ensure they are within valid ranges
    seconds += microseconds // 1000000
    microseconds = microseconds % 1000000
    minutes += seconds // 60
    seconds = seconds % 60
    hours += minutes // 60
    minutes = minutes % 60
    days += hours // 24
    hours = hours % 24
    
    # Return a new relativedelta object with normalized values
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)