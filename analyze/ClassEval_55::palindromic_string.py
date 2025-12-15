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
        दिए गए स्ट्रिंग में सबसे लंबा पलिंड्रोमिक उपस्ट्रिंग खोजता है।
        :return: सबसे लंबा पलिंड्रोमिक उपस्ट्रिंग, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        transformed_string = '|'.join(f'^{self.input_string}$')
        n = len(transformed_string)
        L = [0] * n
        center = right = 0
        
        for i in range(1, n - 1):
            mirror = 2 * center - i
            if right > i:
                L[i] = min(right - i, L[mirror])
            while transformed_string[i + L[i] + 1] == transformed_string[i - L[i] - 1]:
                L[i] += 1
            if i + L[i] > right:
                center, right = i, i + L[i]
        
        max_len = max(L)
        center_index = L.index(max_len)
        start = (center_index - max_len) // 2
        return self.input_string[start:start + max_len]