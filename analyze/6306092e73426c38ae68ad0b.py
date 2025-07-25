def validate_min_max_args(self, args):
    """
    जांचें कि आर्ग्युमेंट्स का मान न्यूनतम और अधिकतम मानों के बीच है या नहीं।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    min_value = 0  # न्यूनतम मान
    max_value = 100  # अधिकतम मान
    
    for arg in args:
        if not (min_value <= arg <= max_value):
            return False
    return True