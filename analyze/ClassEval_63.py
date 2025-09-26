from collections import Counter
import re

class NLPDataProcessor2:

    def process_data(self, string_list):
        return [self.process_string(string) for string in string_list]

    def process_string(self, string):
        processed_string = self.remove_non_english_letters(string)
        return processed_string.split()

    def remove_non_english_letters(self, string):
        return re.sub(r'[^a-zA-Z\s]', '', string.lower())

    def calculate_word_frequency(self, words_list):
        word_frequency = Counter()
        for words in words_list:
            word_frequency.update(words)
        return self.get_top_n_word_frequency(word_frequency, 5)

    def get_top_n_word_frequency(self, word_frequency, n):
        sorted_word_frequency = dict(sorted(word_frequency.items(), key=lambda x: x[1], reverse=True))
        return dict(list(sorted_word_frequency.items())[:n])

    def process(self, string_list):
        words_list = self.process_data(string_list)
        return self.calculate_word_frequency(words_list)