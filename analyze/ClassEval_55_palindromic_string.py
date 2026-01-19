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
    L = [0] * n
    C = R = 0
    for i in range(1, n - 1):
        mirror = 2 * C - i
        if R > i:
            L[i] = min(R - i, L[mirror])
        a, b = (i + (1 + L[i]), i - (1 + L[i]))
        while a < n - 1 and b > 0 and (transformed_string[a] == transformed_string[b]):
            L[i] += 1
            a += 1
            b -= 1
        if i + L[i] > R:
            C, R = (i, i + L[i])
    max_len = max(L)
    center_index = L.index(max_len)
    start = (center_index - max_len) // 2
    return self.input_string[start:start + max_len]