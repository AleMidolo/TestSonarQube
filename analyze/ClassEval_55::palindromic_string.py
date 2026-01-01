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
    transformed = '|' + transformed + '|'
    n = len(transformed)
    pal_len = [0] * n
    max_len = 0
    center_index = 0
    for i in range(n):
        current_len = self.palindromic_length(i, 1, transformed)
        pal_len[i] = current_len
        if current_len > max_len:
            max_len = current_len
            center_index = i
    start = (center_index - max_len) // 2
    end = start + max_len
    return self.input_string[start:end]