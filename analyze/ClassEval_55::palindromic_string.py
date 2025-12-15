class Manacher: 
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

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
        if (center - diff == -1 or center + diff == len(string)
                or string[center - diff] != string[center + diff]):
            return 0
        return 1 + self.palindromic_length(center, diff + 1, string)

    def palindromic_string(self):
        """
        Trova la sottostringa palindromica più lunga nella stringa fornita.
        :return: La sottostringa palindromica più lunga, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        # Transform the input string to avoid even/odd length issues
        transformed_string = '|'.join(f'^{self.input_string}$')
        n = len(transformed_string)
        P = [0] * n
        center = right = 0

        for i in range(1, n - 1):
            mirror = 2 * center - i
            if right > i:
                P[i] = min(right - i, P[mirror])

            # Attempt to expand the palindrome centered at i
            while transformed_string[i + P[i] + 1] == transformed_string[i - P[i] - 1]:
                P[i] += 1

            # If the palindrome centered at i expands past right, adjust center and right
            if i + P[i] > right:
                center, right = i, i + P[i]

        # Find the maximum element in P
        max_length = max(P)
        center_index = P.index(max_length)
        start = (center_index - max_length) // 2  # Adjust for the transformed string
        return self.input_string[start:start + max_length]