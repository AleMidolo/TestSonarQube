def palindromic_string(self):
    """
        Encuentra la subcadena palindrómica más larga en la cadena dada.
        :return: La subcadena palindrómica más larga, str.
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
        left_idx = i - (1 + p[i])
        right_idx = i + (1 + p[i])
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
    start = center_idx - max_len
    end = center_idx + max_len + 1
    palindrome_transformed = transformed[start:end]
    palindrome = palindrome_transformed.replace('|', '')
    return palindrome