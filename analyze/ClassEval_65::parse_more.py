def parse_more(self, i):
    """
        इंडेक्स के आधार पर हज़ार/मिलियन/बिलियन सफ़िक्स को पार्स करता है।

        :param i: int, इंडेक्स जो मैग्नीट्यूड (हज़ार, मिलियन, बिलियन) को दर्शाता है
        :return: str, मैग्नीट्यूड के लिए संबंधित सफ़िक्स

        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
    return self.NUMBER_MORE[i]