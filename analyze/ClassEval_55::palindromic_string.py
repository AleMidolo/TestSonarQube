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
    center = right = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if right > i:
            L[i] = min(right - i, L[mirror])
        while transformed_string[i + L[i] + 1] == transformed_string[i - L[i] - 1]:
            L[i] += 1
        if i + L[i] > right:
            center, right = (i, i + L[i])
    max_length = max(L)
    center_index = L.index(max_length)
    start = (center_index - max_length) // 2
    return self.input_string[start:start + max_length]