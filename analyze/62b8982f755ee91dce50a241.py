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
    
    # Handle fractional parts
    fractional_days = self.days - days
    fractional_hours = self.hours - hours
    fractional_minutes = self.minutes - minutes
    fractional_seconds = self.seconds - seconds
    fractional_microseconds = self.microseconds - microseconds
    
    # Add fractional parts to the next lower unit
    hours += int(fractional_days * 24)
    minutes += int(fractional_hours * 60)
    seconds += int(fractional_minutes * 60)
    microseconds += int(fractional_seconds * 1e6)
    
    # Normalize the values
    seconds += microseconds // 1e6
    microseconds = microseconds % 1e6
    minutes += seconds // 60
    seconds = seconds % 60
    hours += minutes // 60
    minutes = minutes % 60
    days += hours // 24
    hours = hours % 24
    
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)