def normalized(self):
    """
    यह फ़ंक्शन इस ऑब्जेक्ट का एक ऐसा संस्करण लौटाता है, जिसमें सभी सापेक्ष गुण (relative attributes) पूरी तरह से पूर्णांक मानों (integer values) में दर्शाए गए हों।

    उदाहरण:

    >>> relativedelta(days=1.5, hours=2).normalized()
    relativedelta(days=+1, hours=+14)

    :वापसी मान (Return):
    यह एक `dateutil.relativedelta.relativedelta` क्लास का ऑब्जेक्ट लौटाता है।
    """
    total_days = int(self.days) + int(self.hours // 24)
    total_hours = int(self.hours % 24)
    total_minutes = int(self.minutes)
    total_seconds = int(self.seconds)

    return relativedelta(days=total_days, hours=total_hours, minutes=total_minutes, seconds=total_seconds)