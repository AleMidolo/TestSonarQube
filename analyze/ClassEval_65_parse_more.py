def parse_more(self, i):
    """
    इंडेक्स के आधार पर हज़ार/मिलियन/बिलियन सफ़िक्स को पार्स करता है।

    :param i: int, इंडेक्स जो मैग्नीट्यूड (हज़ार, मिलियन, बिलियन) को दर्शाता है
    :return: str, मैग्नीट्यूड के लिए संबंधित सफ़िक्स

    >>> formatter = NumberWordFormatter()
    >>> formatter.parse_more(1)
    "THOUSAND"
    """
    magnitudes = {
        0: "",
        1: "THOUSAND",
        2: "MILLION",
        3: "BILLION",
        4: "TRILLION",
        5: "QUADRILLION",
        6: "QUINTILLION",
        7: "SEXTILLION",
        8: "SEPTILLION",
        9: "OCTILLION",
        10: "NONILLION",
        11: "DECILLION"
    }
    
    return magnitudes.get(i, "")