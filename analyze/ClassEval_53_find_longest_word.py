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
    import string
    
    # Remove punctuation from the sentence
    translator = str.maketrans('', '', string.punctuation)
    cleaned_sentence = sentence.translate(translator)
    
    # Split the sentence into words
    words = cleaned_sentence.split()
    
    # Find the longest word that exists in self.word_list
    longest_word = ''
    
    for word in words:
        if word in self.word_list and len(word) > len(longest_word):
            longest_word = word
    
    return longest_word