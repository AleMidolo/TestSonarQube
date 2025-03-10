def verifyClass(iface, candidate, tentative=False):
    """
    यह फ़ंक्शन सत्यापित करता है कि *candidate* सही तरीके से *iface* प्रदान कर सकता है या नहीं।
    """
    if tentative:
        # Tentative mode: Check if candidate has all the methods of iface
        for method in dir(iface):
            if not method.startswith('__') and not hasattr(candidate, method):
                return False
        return True
    else:
        # Strict mode: Check if candidate is a subclass of iface
        return issubclass(candidate, iface)