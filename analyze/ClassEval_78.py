import re


class SplitSentence:

    def split_sentences(self, sentences_string):
        return re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sentences_string)

    def count_words(self, sentence):
        cleaned_sentence = self._clean_sentence(sentence)
        return len(cleaned_sentence.split())

    def _clean_sentence(self, sentence):
        return re.sub(r'[^a-zA-Z\s]', '', sentence)

    def process_text_file(self, sentences_string):
        sentences = self.split_sentences(sentences_string)
        return self._find_max_word_count(sentences)

    def _find_max_word_count(self, sentences):
        return max(self.count_words(sentence) for sentence in sentences)