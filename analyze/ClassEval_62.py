class NLPDataProcessor:

    STOP_WORDS = {'a', 'an', 'the'}

    def remove_stop_words(self, string_list):
        return [self._remove_stop_words_from_string(string) for string in string_list]

    def _remove_stop_words_from_string(self, string):
        string_split = string.split()
        return [word for word in string_split if word not in self.STOP_WORDS]

    def process(self, string_list):
        return self.remove_stop_words(string_list)