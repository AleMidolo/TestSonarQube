def status_str(self, prefix=''):
    """
    वैलिडेटर की स्थिति की स्ट्रिंग लौटाएं, जिसमें वैकल्पिक `prefix` जोड़ा जा सकता है।
    """
    status = "Valid" if self.is_valid else "Invalid"
    if prefix:
        return f"{prefix}: {status}"
    return status