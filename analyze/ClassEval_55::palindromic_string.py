def palindromic_string(self):
    """
        Trova la sottostringa palindromica più lunga nella stringa fornita.
        :return: La sottostringa palindromica più lunga, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'

        """
    if not self.input_string:
        return ''
    transformed = '|'.join(self.input_string)
    p = [0] * len(transformed)
    center = 0
    right = 0
    for i in range(len(transformed)):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])
        while i - p[i] - 1 >= 0 and i + p[i] + 1 < len(transformed) and (transformed[i - p[i] - 1] == transformed[i + p[i] + 1]):
            p[i] += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
    max_len = 0
    center_index = 0
    for i in range(len(p)):
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    start = (center_index - max_len) // 2
    end = start + max_len
    return self.input_string[start:end]