import re

class SplitSentence: 

    def split_sentences(self, sentences_string):
        """
        Split a string into a list of sentences. Sentences end with . or ? and with a space after that. Please note that Mr. also end with . but are not sentences.
        :param sentences_string: string, string to split
        :return:list, split sentence list
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
        sentences = re.split(
            r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', sentences_string)
        return sentences
    
    def process_text_file(self, sentences_string):
        """
        Given a text, return the number of words in the longest sentence
        :param sentences_string: string, undivided long sentence
        :return:int, the number of words in the longest sentence
        >>> ss = SplitSentence()
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        sentences = self.split_sentences(sentences_string)
        max_count = 0
        for sentence in sentences:
            count = self.count_words(sentence)
            if count > max_count:
                max_count = count
    
        return max_count
    
    def count_words(self, sentence):
        """
        Conta il numero di parole in una frase. Nota che le parole sono separate da spazi e che i segni di punteggiatura e i numeri non sono conteggiati come parole.
        :param sentence:string, frase da contare, dove le parole sono separate da spazi
        :return:int, numero di parole nella frase
        >>> ss = SplitSentence()
        >>> ss.count_words("abc def")
        2
        """
        return len([word for word in sentence.split() if word.isalpha()])