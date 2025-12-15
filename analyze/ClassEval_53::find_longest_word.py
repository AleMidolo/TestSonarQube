import re
import string

class LongestWord: 
    def __init__(self):
        """
        Initialize a list of word.
        """
        self.word_list = []

    def add_word(self, word):
        """
        append the input word into self.word_list
        :param word: str, input word
        """
        self.word_list.append(word)
    
    def find_longest_word(self, sentence):
        """
        विराम चिह्नों को हटाएं और एक वाक्य को शब्दों की सूची में विभाजित करें। self.word_list में जो सबसे लंबा विभाजित शब्द है, उसे खोजें।
        शब्द पूरी तरह से केस-संवेदनशील होते हैं।
        :param sentence: एक वाक्य str
        :return str: सबसे लंबा विभाजित शब्द जो self.word_list में है। यदि self.word_list खाली है तो '' लौटाएं।
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        
        # Find the longest word in self.word_list that is in the words from the sentence
        longest = ''
        for word in words:
            if word in self.word_list and len(word) > len(longest):
                longest = word
        
        return longest