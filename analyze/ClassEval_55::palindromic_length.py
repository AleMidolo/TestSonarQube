class Manacher: 
    def __init__(self, input_string) -> None:
        """
        Initializes the Manacher class with the given input_string.
        :param input_string: The input_string to be searched, str.
        """
        self.input_string = input_string

    def palindromic_string(self):
        """
        Finds the longest palindromic substring in the given string.
        :return: The longest palindromic substring, str.
        >>> manacher = Manacher('ababaxse')
        >>> manacher.palindromic_string()
        'ababa'
        """
        max_length = 0
        new_input_string = ""
        output_string = ""

        for i in self.input_string[:len(self.input_string) - 1]:
            new_input_string += i + "|"
        new_input_string += self.input_string[-1]

        for i in range(len(new_input_string)):
            length = self.palindromic_length(i, 1, new_input_string)

            if max_length < length:
                max_length = length
                start = i

        for i in new_input_string[start - max_length:start + max_length + 1]:
            if i != "|":
                output_string += i

        return output_string

    def palindromic_length(self, center, diff, string):
        """
        Calcola ricorsivamente la lunghezza della sottostringa palindromica basata su un centro dato, un valore di differenza e una stringa di input.
        :param center: Il centro della sottostringa palindromica, int.
        :param diff: La differenza tra il centro e la posizione attuale, int.
        :param string: La stringa da cercare, str.
        :return: La lunghezza della sottostringa palindromica, int.
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2
        """
        left = center - diff
        right = center + diff
        while left >= 0 and right < len(string) and string[left] == string[right]:
            diff += 1
            left -= 1
            right += 1
        return diff - 1