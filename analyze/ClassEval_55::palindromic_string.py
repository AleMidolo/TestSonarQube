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
        while transformed_string[i + p[i] + 1] == transformed_string[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
        max_len = max(max_len, p[i])
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    return self.input_string[start:start + max_len]