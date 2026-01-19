import string
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def lemmatize_sentence(self, sentence):
    """
    पंक्चुएशन हटाता है और इनपुट सेंटेंस को टोकनाइज़ करता है।
    हर शब्द को पार्ट-ऑफ़-स्पीच टैग से मार्क करता है।
    फिर उनके पार्ट-ऑफ़-स्पीच के आधार पर अलग-अलग पैरामीटर के साथ लेमेटाइज़ करता है,
    और उन्हें एक लिस्ट में स्टोर करता है।

    :param sentence: str, एक इनपुट सेंटेंस
    :return: list, लेमेटाइज़ किए गए शब्दों की लिस्ट

    >>> lemmatization = Lemmatization()
    >>> lemmatization.lemmatize_sentence("I am running in a race.")
    ['I', 'to be', 'running', 'in', 'a', 'race']
    """
    # Remove punctuation
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Get POS tags
    pos_tags = nltk.pos_tag(tokens)
    
    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Helper function to convert Penn Treebank tags to WordNet tags
    def get_wordnet_pos(treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN  # Default to noun
    
    # Lemmatize each word based on its POS tag
    lemmatized_words = []
    for word, pos in pos_tags:
        wordnet_pos = get_wordnet_pos(pos)
        lemmatized_word = lemmatizer.lemmatize(word, pos=wordnet_pos)
        lemmatized_words.append(lemmatized_word)
    
    return lemmatized_words