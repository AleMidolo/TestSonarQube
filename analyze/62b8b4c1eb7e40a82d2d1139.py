def verifyClass(iface, candidate, tentative=False):
    """
    यह फ़ंक्शन सत्यापित करता है कि *candidate* सही तरीके से *iface* प्रदान कर सकता है या नहीं।
    """
    if not tentative:
        return issubclass(candidate, iface)
    else:
        try:
            return issubclass(candidate, iface)
        except TypeError:
            return False