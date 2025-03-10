def verifyClass(iface, candidate, tentative=False):
    """
    यह फ़ंक्शन सत्यापित करता है कि *candidate* सही तरीके से *iface* प्रदान कर सकता है या नहीं।
    """
    if not tentative:
        return all(hasattr(candidate, attr) and callable(getattr(candidate, attr)) for attr in dir(iface) if not attr.startswith('__'))
    else:
        return all(hasattr(candidate, attr) for attr in dir(iface) if not attr.startswith('__'))