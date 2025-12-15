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
        Rimuove i segni di punteggiatura e suddivide una frase in un elenco di parole. Trova la parola suddivisa più lunga che si trova in self.word_list.
        Le parole sono strettamente sensibili al maiuscolo/minuscolo.
        :param sentence: una frase str
        :return str: la parola suddivisa più lunga che si trova in self.word_list. restituisce '' se self.word_list è vuota.
        >>> longestWord = LongestWord()
        >>> longestWord.add_word('A')
        >>> longestWord.add_word('aM')
        >>> longestWord.find_longest_word('I am a student.')
        'a'
        """
        # Remove punctuation and split the sentence into words
        words = re.findall(r'\b\w+\b', sentence)
        
        if not self.word_list:
            return ''
        
        longest = ''
        for word in words:
            if word in self.word_list and len(word) > len(longest):
                longest = word
        
        return longest