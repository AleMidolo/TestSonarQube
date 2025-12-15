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
    
    def count_words(self, sentence):
        """
        Count the number of words in a sentence. Note that words are separated by spaces and that punctuation marks and numbers are not counted as words.
        :param sentence:string, sentence to be counted, where words are separated by spaces
        :return:int, number of words in the sentence
        >>> ss.count_words("abc def")
        2
        """
    
        sentence = re.sub(r'[^a-zA-Z\s]', '', sentence)
        words = sentence.split()
        return len(words)
    
    def process_text_file(self, sentences_string):
        """
        दिए गए पाठ के लिए, सबसे लंबे वाक्य में शब्दों की संख्या लौटाएं
        :param sentences_string: स्ट्रिंग, अविभाजित लंबा वाक्य
        :return:int, सबसे लंबे वाक्य में शब्दों की संख्या
        >>> ss = SplitSentence()
        >>> ss.process_text_file("aaa aaaa. bb bbbb bbb? cccc ccccccc cc ccc. dd ddd?")
        4
        """
        
        sentences = self.split_sentences(sentences_string)
        max_words = 0
        for sentence in sentences:
            word_count = self.count_words(sentence)
            if word_count > max_words:
                max_words = word_count
        return max_words