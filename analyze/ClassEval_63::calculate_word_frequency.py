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
        计算词汇表中每个单词的词频，并按值降序排序词频字典。
        :param words_list: 一个单词列表的列表
        :return: 前5个词频字典，一个词频字典，键是单词，值是频率
        >>> NLPDataProcessor2().calculate_word_frequency([['this', 'is', 'a', 'test'], ['this', 'is', 'another', 'test']])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
        
        # Flatten the list of words
        flat_list = [word for sublist in words_list for word in sublist]
        # Calculate word frequency
        word_count = Counter(flat_list)
        # Sort by frequency and get the top 5
        sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
        return dict(list(sorted_word_count.items())[:5])