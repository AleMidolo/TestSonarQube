import re


class SplitSentence:

    def split_sentences(self, sentences_string):
        return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sentences_string)

    def count_words(self, sentence):
        cleaned_sentence = self._remove_non_alpha(sentence)
        words = cleaned_sentence.split()
        return len(words)

    def _remove_non_alpha(self, sentence):
        return re.sub(r'[^a-zA-Z\s]', '', sentence)

    def process_text_file(self, sentences_string):
        sentences = self.split_sentences(sentences_string)
        return self._find_max_word_count(sentences)

    def _find_max_word_count(self, sentences):
        max_count = 0
        for sentence in sentences:
            count = self.count_words(sentence)
            if count > max_count:
                max_count = count
        return max_count