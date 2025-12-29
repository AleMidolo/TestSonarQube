def palindromic_string(self):
    """
        在给定的字符串中找到最长的回文子串。
        :return: 最长的回文子串，str。
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
    transformed = '|'.join(f'^{self.input_string}$')
    n = len(transformed)
    p = [0] * n
    center = right = 0
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while transformed[i + p[i] + 1] == transformed[i - p[i] - 1]:
            p[i] += 1
        if i + p[i] > right:
            center, right = (i, i + p[i])
    max_length = max(p)
    center_index = p.index(max_length)
    start = (center_index - max_length) // 2
    return self.input_string[start:start + max_length]