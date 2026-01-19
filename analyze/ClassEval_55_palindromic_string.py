def palindromic_string(self):
    """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
    if not self.input_string:
        return ''
    transformed = '|' + '|'.join(self.input_string) + '|'
    n = len(transformed)
    p = [0] * n
    center = 0
    right = 0
    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and (transformed[i - p[i] - 1] == transformed[i + p[i] + 1]):
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
    max_len = max(p)
    max_center = p.index(max_len)
    start = (max_center - max_len) // 2
    end = start + max_len
    return self.input_string[start:end]