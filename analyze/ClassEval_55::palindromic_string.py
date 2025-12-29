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
    p = [0] * n
    center = right = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if right > i:
            p[i] = min(right - i, p[mirror])
        while transformed_string[i + p[i] + 1] == transformed_string[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = (i, i + p[i])
    max_length = max(p)
    center_index = p.index(max_length)
    start = (center_index - max_length) // 2
    return self.input_string[start:start + max_length]