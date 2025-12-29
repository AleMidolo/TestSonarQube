def parse_more(self, i):
    """
        Parses the thousand/million/billion suffix based on the index.

        :param i: int, the index representing the magnitude (thousand, million, billion)
        :return: str, the corresponding suffix for the magnitude

        >>> formatter = NumberWordFormatter()
        >>> formatter.parse_more(1)
        "THOUSAND"
        """
    return self.NUMBER_MORE[i] if i < len(self.NUMBER_MORE) else ''