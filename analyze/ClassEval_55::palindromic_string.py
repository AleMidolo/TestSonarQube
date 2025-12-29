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
    P = [0] * n
    center = right = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if right > i:
            P[i] = min(right - i, P[mirror])
        while transformed_string[i + P[i] + 1] == transformed_string[i - P[i] - 1]:
            P[i] += 1
        if i + P[i] > right:
            center, right = (i, i + P[i])
    max_length = max(P)
    center_index = P.index(max_length)
    start = (center_index - max_length) // 2
    return self.input_string[start:start + max_length]