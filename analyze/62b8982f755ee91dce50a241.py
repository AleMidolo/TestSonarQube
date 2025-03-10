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
    years = int(self.years)
    months = int(self.months)
    
    # Create a new relativedelta object with normalized values
    return relativedelta(years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)