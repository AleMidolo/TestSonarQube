def validate_min_max_args(self, args):
    """
    जांचें कि आर्ग्युमेंट्स का मान न्यूनतम और अधिकतम मानों के बीच है या नहीं।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    min_value = self.min_value  # Assuming min_value is defined in the class
    max_value = self.max_value  # Assuming max_value is defined in the class

    for arg in args:
        if not (min_value <= arg <= max_value):
            return False
    return True