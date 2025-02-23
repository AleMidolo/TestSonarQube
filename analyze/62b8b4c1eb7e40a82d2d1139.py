def verifyClass(iface, candidate, tentative=False):
    """
    यह फ़ंक्शन सत्यापित करता है कि *candidate* सही तरीके से *iface* प्रदान कर सकता है या नहीं।
    """
    if tentative:
        return issubclass(candidate, iface) or iface in candidate.__bases__
    return isinstance(candidate, iface)