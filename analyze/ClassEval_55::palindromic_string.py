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
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
        transformed_string = '|'.join(f'^{self.input_string}$')
        n = len(transformed_string)
        max_len = 0
        center = 0
        right = 0
        p = [0] * n

        for i in range(1, n - 1):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])

            a, b = i + (1 + p[i]), i - (1 + p[i])
            while a < n - 1 and b > 0 and transformed_string[a] == transformed_string[b]:
                p[i] += 1
                a += 1
                b -= 1

            if i + p[i] > right:
                center, right = i, i + p[i]

            max_len = max(max_len, p[i])

        start = (max_len * 2) // 2
        return self.input_string[start - max_len:start + max_len].replace('|', '')