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
    max_length = 0
    center_index = 0
    for i in range(len(transformed)):
        length = self.palindromic_length(i, 1, transformed)
        if length > max_length:
            max_length = length
            center_index = i
    start = (center_index - max_length) // 2
    end = start + max_length
    return self.input_string[start:end]