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
        # Keep only English letters and spaces
        filtered_string = ''.join(char for char in string if char.isalpha() or char.isspace())
        
        # Convert to lowercase
        lowercase_string = filtered_string.lower()
        
        # Split into words
        words = lowercase_string.split()
        
        words_list.append(words)
    
    return words_list