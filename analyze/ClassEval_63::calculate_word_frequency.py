from collections import Counter
import re

class NLPDataProcessor2: 

    def process_data(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words.
        :param string_list: a list of strings
        :return: words_list: a list of words lists
        >>> NLPDataProcessor2().process_data(['This is a test.'])
        [['this', 'is', 'a', 'test']]
        """
    
        words_list = []
        for string in string_list:
            # Remove non-English letters and convert to lowercase
            processed_string = re.sub(r'[^a-zA-Z\s]', '', string.lower())
            # Split the string into words
            words = processed_string.split()
            words_list.append(words)
        return words_list
    
    def process(self, string_list):
        """
        keep only English letters and spaces in the string, then convert the string to lower case, and then split the string into a list of words. Calculate the word frequency of each word in the list of words list, and sort the word frequency dictionary by value in descending order.
        :param string_list: a list of strings
        :return: top 5 word frequency dictionary, a dictionary of word frequency, key is word, value is frequency
        >>> NLPDataProcessor2().process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    
        words_list = self.process_data(string_list)
        word_frequency_dict = self.calculate_word_frequency(words_list)
        return word_frequency_dict
    
    def calculate_word_frequency(self, words_list):
        """
        शब्दों की सूची में प्रत्येक शब्द की शब्द आवृत्ति की गणना करें, और शब्द आवृत्ति शब्दकोश को मान के अनुसार अवरोही क्रम में क्रमबद्ध करें।
        :param words_list: शब्दों की सूचियों की एक सूची
        :return: शीर्ष 5 शब्द आवृत्ति शब्दकोश, एक शब्द आवृत्ति का शब्दकोश, कुंजी शब्द है, मान आवृत्ति है
        >>> NLPDataProcessor2().calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        
        flat_list = [word for sublist in words_list for word in sublist]
        word_count = Counter(flat_list)
        sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        return dict(list(sorted_word_count.items())[:5])