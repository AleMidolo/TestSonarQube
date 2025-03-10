def validate_min_max_args(self, args):
    """
    जांचें कि आर्ग्युमेंट्स का मान न्यूनतम और अधिकतम मानों के बीच है या नहीं।

    :param args: प्राप्त किए गए आर्ग्युमेंट्स।
    """
    if not hasattr(self, 'min_value') or not hasattr(self, 'max_value'):
        raise ValueError("min_value और max_value को परिभाषित करें।")
    
    for arg in args:
        if not (self.min_value <= arg <= self.max_value):
            return False
    return True