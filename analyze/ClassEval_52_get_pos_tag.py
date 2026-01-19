import string
import nltk
from nltk import pos_tag, word_tokenize

def get_pos_tag(self, sentence):
    """
    वाक्य से पंक्चुएशन हटाएँ और इनपुट वाक्य को टोकनाइज़ करें,
    फिर हर शब्द के लिए पार्ट-ऑफ़-स्पीच (POS) टैग को मार्क करें।

    :param sentence: str, एक वाक्य
    :return: list, वाक्य में हर शब्द के लिए POS टैग

    >>> lemmatization = Lemmatization()
    >>> lemmatization.get_pos_tag("मैं एक रेस में दौड़ रहा हूँ।")
    ['PRP', 'VBP', 'VBG', 'IN', 'DT', 'NN']
    """
    # Remove punctuation from the sentence
    translator = str.maketrans('', '', string.punctuation)
    sentence_no_punct = sentence.translate(translator)
    
    # Tokenize the sentence
    tokens = word_tokenize(sentence_no_punct)
    
    # Get POS tags for each token
    pos_tags = pos_tag(tokens)
    
    # Extract only the tags (second element of each tuple)
    tags_only = [tag for word, tag in pos_tags]
    
    return tags_only