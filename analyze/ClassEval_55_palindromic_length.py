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
    left = center - diff
    right = center + diff
    while left >= 0 and right < len(string) and (string[left] == string[right]):
        diff += 1
        left -= 1
        right += 1
    return diff - 1