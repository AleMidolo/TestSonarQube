def format_string(self, x):
    """
        एक संख्या के स्ट्रिंग प्रतिनिधित्व को शब्दों के प्रारूप में परिवर्तित करता है
        :param x: str, संख्या का स्ट्रिंग प्रतिनिधित्व
        :return: str, संख्या शब्दों के प्रारूप में
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "एक सौ और तेईस हजार चार सौ और छप्पन केवल"
        """
    if x.startswith('-'):
        return 'MINUS ' + self.format_string(x[1:])
    if '.' in x:
        integer_part, decimal_part = x.split('.')
        integer_words = self._format_integer_part(integer_part)
        decimal_words = self._format_decimal_part(decimal_part)
        if integer_words:
            return f'{integer_words} AND {decimal_words} ONLY'
        else:
            return f'{decimal_words} ONLY'
    else:
        integer_words = self._format_integer_part(x)
        if integer_words:
            return f'{integer_words} ONLY'
        else:
            return 'ZERO ONLY'