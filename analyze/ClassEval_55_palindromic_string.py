def palindromic_string(self):
    """
        Trova la sottostringa palindromica più lunga nella stringa fornita.
        :return: La sottostringa palindromica più lunga, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
    transformed_string = '|'.join(f'^{self.input_string}$')
    n = len(transformed_string)
    max_len = 0
    center = 0
    right = 0
    lengths = [0] * n
    for i in range(1, n - 1):
        mirror = 2 * center - i
        if i < right:
            lengths[i] = min(right - i, lengths[mirror])
        a, b = (i + (1 + lengths[i]), i - (1 + lengths[i]))
        while a < n - 1 and b > 0 and (transformed_string[a] == transformed_string[b]):
            lengths[i] += 1
            a += 1
            b -= 1
        if i + lengths[i] > right:
            center, right = (i, i + lengths[i])
        if lengths[i] > max_len:
            max_len = lengths[i]
    start = max_len * 2 // 2
    return self.input_string[start - max_len:start + max_len + 1]