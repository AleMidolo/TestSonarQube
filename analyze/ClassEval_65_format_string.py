def format_string(self, x):
    """
        एक संख्या के स्ट्रिंग प्रतिनिधित्व को शब्दों के प्रारूप में परिवर्तित करता है
        :param x: str, संख्या का स्ट्रिंग प्रतिनिधित्व
        :return: str, संख्या शब्दों के प्रारूप में
        >>> formatter = NumberWordFormatter()
        >>> formatter.format_string("123456")
        "एक सौ और तेईस हजार चार सौ और छप्पन केवल"
        """
    if not x:
        return ''
    is_negative = False
    if x[0] == '-':
        is_negative = x[0] == '-'
        x = x[1:]
    parts = x.split('.')
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ''
    integer_part = integer_part.lstrip('0')
    if integer_part == '':
        integer_part = '0'
    integer_words = self._convert_integer_part(integer_part)
    decimal_words = ''
    if decimal_part:
        decimal_words = self._convert_decimal_part(decimal_part)
    result = ''
    if is_negative:
        result += 'MINUS '
    result += integer_words
    if decimal_words:
        result += ' AND ' + decimal_words + ' CENTS'
    else:
        result += ' ONLY'
    return result