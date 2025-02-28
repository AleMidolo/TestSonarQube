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
    
    # Calculate the remaining hours, minutes, seconds, and microseconds
    remaining_hours = int((self.days - days) * 24)
    remaining_minutes = int((self.hours - hours) * 60)
    remaining_seconds = int((self.minutes - minutes) * 60)
    remaining_microseconds = int((self.seconds - seconds) * 1e6)
    
    # Add the remaining values to the respective attributes
    hours += remaining_hours
    minutes += remaining_minutes
    seconds += remaining_seconds
    microseconds += remaining_microseconds
    
    # Normalize the values
    minutes += seconds // 60
    seconds = seconds % 60
    hours += minutes // 60
    minutes = minutes % 60
    days += hours // 24
    hours = hours % 24
    
    # Return the normalized relativedelta object
    return relativedelta(days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)