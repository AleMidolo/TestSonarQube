def process(self, string_list):
    """
        स्ट्रिंग में केवल अंग्रेजी अक्षर और स्पेस रखें, फिर स्ट्रिंग को लोअर केस में बदलें, और फिर स्ट्रिंग को शब्दों की सूची में विभाजित करें। शब्दों की सूची में प्रत्येक शब्द की शब्द आवृत्ति की गणना करें, और शब्द आवृत्ति शब्दकोश को मान के अनुसार अवरोही क्रम में सॉर्ट करें।
        :param string_list: स्ट्रिंग की एक सूची
        :return: शीर्ष 5 शब्द आवृत्ति शब्दकोश, शब्द आवृत्ति का एक शब्दकोश, कुंजी शब्द है, मान आवृत्ति है
        >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
        {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
        """
    words_list = self.process_data(string_list)
    return self.calculate_word_frequency(words_list)