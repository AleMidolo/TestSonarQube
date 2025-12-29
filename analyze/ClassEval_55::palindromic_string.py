def palindromic_string(self):
    """
        दिए गए स्ट्रिंग में सबसे लंबा पलिंड्रोमिक उपस्ट्रिंग खोजता है।
        :return: सबसे लंबा पलिंड्रोमिक उपस्ट्रिंग, str.
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
        left_idx = i - (p[i] + 1)
        right_idx = i + (p[i] + 1)
        while left_idx >= 0 and right_idx < len(transformed) and (transformed[left_idx] == transformed[right_idx]):
            p[i] += 1
            left_idx -= 1
            right_idx += 1
        if i + p[i] > right:
            center = i
            right = i + p[i]
    max_len = 0
    center_idx = 0
    for i in range(len(p)):
        if p[i] > max_len:
            max_len = p[i]
            center_idx = i
    start = (center_idx - max_len) // 2
    end = start + max_len
    return self.input_string[start:end]