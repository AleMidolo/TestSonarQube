class NLPDataProcessor:

    def construct_stop_word_list(self):
        return ['a', 'an', 'the']

    def remove_stop_words(self, string_list):
        stop_word_list = self.construct_stop_word_list()
        return [self._remove_stop_words_from_string(string, stop_word_list) for string in string_list]

    def _remove_stop_words_from_string(self, string, stop_word_list):
        string_split = string.split()
        return [word for word in string_split if word not in stop_word_list]

    def process(self, string_list):
        return self.remove_stop_words(string_list)