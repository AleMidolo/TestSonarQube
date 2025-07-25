import re
import string


class LongestWord:

    def __init__(self):
        self.word_list = []

    def add_word(self, word):
        self.word_list.append(word)

    def find_longest_word(self, sentence):
        cleaned_sentence = self.clean_sentence(sentence)
        return self.get_longest_word(cleaned_sentence)

    def clean_sentence(self, sentence):
        sentence = sentence.lower()
        sentence = re.sub('[%s]' % re.escape(string.punctuation), '', sentence)
        return re.split(' ', sentence)

    def get_longest_word(self, words):
        longest_word = ""
        for word in words:
            if word in self.word_list and len(word) > len(longest_word):
                longest_word = word
        return longest_word