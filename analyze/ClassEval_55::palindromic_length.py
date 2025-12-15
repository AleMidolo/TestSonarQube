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
        递归计算基于给定中心、差值和输入字符串的回文子串的长度。
        :param center: 回文子串的中心，int。
        :param diff: 中心与当前位之间的差值，int。
        :param string: 要搜索的字符串，str。
        :return: 回文子串的长度，int。
        >>> manacher = Manacher('ababa')
        >>> manacher.palindromic_length(2, 1, 'a|b|a|b|a')
        2
        """
        if center - diff < 0 or center + diff >= len(string):
            return diff - 1
        if string[center - diff] == string[center + diff]:
            return self.palindromic_length(center, diff + 1, string)
        return diff - 1