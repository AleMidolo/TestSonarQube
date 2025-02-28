def status_str(self, prefix=''):
    """
    वैलिडेटर की स्थिति की स्ट्रिंग लौटाएं, जिसमें वैकल्पिक `prefix` जोड़ा जा सकता है।
    """
    # Assuming the validator has a status attribute
    return f"{prefix}{self.status}"