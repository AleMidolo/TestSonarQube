def palindromic_string(self):
    """
        Encuentra la subcadena palindrómica más larga en la cadena dada.
        :return: La subcadena palindrómica más larga, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
    transformed = '|'.join(f'^{self.input_string}$')
    n = len(transformed)
    L = [0] * n
    C = R = 0
    for i in range(1, n - 1):
        mirror = 2 * C - i
        if R > i:
            L[i] = min(R - i, L[mirror])
        while transformed[i + L[i] + 1] == transformed[i - L[i] - 1]:
            L[i] += 1
        if i + L[i] > R:
            C, R = (i, i + L[i])
    max_len = max(L)
    center_index = L.index(max_len)
    start = (center_index - max_len) // 2
    return self.input_string[start:start + max_len]