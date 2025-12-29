def palindromic_length(self, center, diff, string):
    """
        Recursively calculates the length of the palindromic substring based on a given center, difference value, and input string.
        :param center: The center of the palindromic substring, int.
        :param diff: The difference between the center and the current position, int.
        :param string: The string to be searched, str.
        :return: The length of the palindromic substring, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2

        """
    if center - diff == -1 or center + diff == len(string):
        return 0
    if string[center - diff] == string[center + diff]:
        return 1 + self.palindromic_length(center, diff + 1, string)
    else:
        return 0