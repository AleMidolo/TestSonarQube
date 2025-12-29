def palindromic_string(self):
    """
        在给定的字符串中找到最长的回文子串。
        :return: 最长的回文子串，str。
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
    if not self.input_string:
        return ''
    transformed = '|'.join(self.input_string)
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
    max_len = 0
    center_index = 0
    for i in range(n):
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    start = (center_index - max_len) // 2
    end = start + max_len
    return self.input_string[start:end]