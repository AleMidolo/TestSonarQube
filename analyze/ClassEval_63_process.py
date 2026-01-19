def process(self, string_list):
    """
    स्ट्रिंग में केवल अंग्रेजी अक्षर और स्पेस रखें, फिर स्ट्रिंग को लोअर केस में बदलें, और फिर स्ट्रिंग को शब्दों की सूची में विभाजित करें। शब्दों की सूची में प्रत्येक शब्द की शब्द आवृत्ति की गणना करें, और शब्द आवृत्ति शब्दकोश को मान के अनुसार अवरोही क्रम में सॉर्ट करें।
    :param string_list: स्ट्रिंग की एक सूची
    :return: शीर्ष 5 शब्द आवृत्ति शब्दकोश, शब्द आवृत्ति का एक शब्दकोश, कुंजी शब्द है, मान आवृत्ति है
    >>> NLPDataProcessor.process(['This is a test.', 'This is another test.'])
    {'this': 2, 'is': 2, 'test': 2, 'a': 1, 'another': 1}
    """
    word_freq = {}
    
    for string in string_list:
        # Keep only English letters and spaces
        cleaned = ''.join(char if char.isalpha() or char.isspace() else '' for char in string)
        
        # Convert to lowercase
        cleaned = cleaned.lower()
        
        # Split into words
        words = cleaned.split()
        
        # Count word frequency
        for word in words:
            if word:  # Skip empty strings
                word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency in descending order and get top 5
    sorted_freq = dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5])
    
    return sorted_freq