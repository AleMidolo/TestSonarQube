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
        在给定的字符串中找到最长的回文子串。
        :return: 最长的回文子串，str。
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        # Transform the input string to avoid even/odd length issues
        transformed = '|'.join(f'^{self.input_string}$')
        n = len(transformed)
        p = [0] * n
        center = right = 0
        
        for i in range(1, n - 1):
            mirror = 2 * center - i
            
            if i < right:
                p[i] = min(right - i, p[mirror])
            
            # Attempt to expand the palindrome centered at i
            while transformed[i + p[i] + 1] == transformed[i - p[i] - 1]:
                p[i] += 1
            
            # If the palindrome expanded past the right edge, adjust the center and right edge
            if i + p[i] > right:
                center, right = i, i + p[i]
        
        # Find the maximum element in p
        max_length = max(p)
        center_index = p.index(max_length)
        
        # Extract the longest palindromic substring
        start = (center_index - max_length) // 2
        return self.input_string[start:start + max_length]