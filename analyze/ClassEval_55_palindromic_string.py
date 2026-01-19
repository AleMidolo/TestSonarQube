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
    transformed = '|' + transformed + '|'
    max_length = 0
    max_center = 0
    for center in range(len(transformed)):
        length = self.palindromic_length(center, 1, transformed)
        if length > max_length:
            max_length = length
            max_center = center
    start = (max_center - max_length) // 2
    end = start + max_length
    return self.input_string[start:end]