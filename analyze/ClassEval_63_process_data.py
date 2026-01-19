def process_data(self, string_list):
    """
        स्ट्रिंग में केवल अंग्रेजी अक्षर और स्पेस रखें, फिर स्ट्रिंग को लोअर केस में बदलें, और फिर स्ट्रिंग को शब्दों की सूची में विभाजित करें।
        :param string_list: स्ट्रिंग की एक सूची
        :return: words_list: शब्दों की सूचियों की एक सूची
        >>> NLPDataProcessor.process_data(['This is a test.'])
        [['this', 'is', 'a', 'test']]
        """
    words_list = []
    for string in string_list:
        cleaned_string = re.sub('[^a-zA-Z\\s]', '', string)
        lower_string = cleaned_string.lower()
        words = [word for word in lower_string.split() if word]
        words_list.append(words)
    return words_list