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
    lps = [0] * n
    center = right = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if right > i:
            lps[i] = min(right - i, lps[mirror])
        while transformed_string[i + lps[i] + 1] == transformed_string[i - lps[i] - 1]:
            lps[i] += 1
        if i + lps[i] > right:
            center, right = (i, i + lps[i])
    max_length = max(lps)
    center_index = lps.index(max_length)
    start = (center_index - max_length) // 2
    return self.input_string[start:start + max_length]