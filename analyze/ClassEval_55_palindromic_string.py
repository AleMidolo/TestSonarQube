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
        a, b = (i + (1 + p[i]), i - (1 + p[i]))
        while a < n - 1 and b > 0 and (transformed_string[a] == transformed_string[b]):
            p[i] += 1
            a += 1
            b -= 1
        if i + p[i] > right:
            center, right = (i, i + p[i])
        max_len = max(max_len, p[i])
    start = max_len * 2 // 2
    return self.input_string[start - max_len:start + max_len].replace('|', '')