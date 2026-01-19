def parse_more(self, i):
    """
    Parses the thousand/million/billion suffix based on the index
    :param i: int, the index representing the magnitude (thousand, million, billion)
    :return: str, the corresponding suffix for the magnitude
    >>> formatter = NumberWordFormatter()
    >>> formatter.parse_more(1)
    "THOUSAND"
    """
    magnitudes = {
        1: "THOUSAND",
        2: "MILLION",
        3: "BILLION"
    }
    return magnitudes.get(i, "")