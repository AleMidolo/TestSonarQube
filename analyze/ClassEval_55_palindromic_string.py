def palindromic_string(self):
    """
        在给定的字符串中找到最长的回文子串。
        :return: 最长的回文子串，str。
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
        while transformed_string[i + L[i] + 1] == transformed_string[i - L[i] - 1]:
            L[i] += 1
        if i + L[i] > R:
            C, R = (i, i + L[i])
    max_len = max(L)
    center_index = L.index(max_len)
    start = (center_index - max_len) // 2
    return self.input_string[start:start + max_len]