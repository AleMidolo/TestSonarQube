class Manacher:
    def __init__(self, input_string) -> None:
        self.input_string = input_string

    def palindromic_length(self, center, diff, string):
        if self.is_palindrome_boundary(center, diff, string):
            return 0
        return 1 + self.palindromic_length(center, diff + 1, string)

    def is_palindrome_boundary(self, center, diff, string):
        return (center - diff == -1 or center + diff == len(string) or 
                string[center - diff] != string[center + diff])

    def palindromic_string(self):
        new_input_string = self.prepare_input_string()
        max_length, start = self.find_longest_palindrome(new_input_string)
        return self.extract_palindrome(new_input_string, start, max_length)

    def prepare_input_string(self):
        return "|".join(self.input_string) + "|"  # Add separator between characters

    def find_longest_palindrome(self, new_input_string):
        max_length = 0
        start = 0

        for i in range(len(new_input_string)):
            length = self.palindromic_length(i, 1, new_input_string)

            if max_length < length:
                max_length = length
                start = i

        return max_length, start

    def extract_palindrome(self, new_input_string, start, max_length):
        return ''.join(i for i in new_input_string[start - max_length:start + max_length + 1] if i != "|")