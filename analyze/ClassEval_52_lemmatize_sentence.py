import string
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def lemmatize_sentence(self, sentence):
    """
    Remove punctuations of the sentence and tokenizes the input sentence, mark the part of speech tag of each word,
    lemmatizes the words with different parameters based on their parts of speech, and stores in a list.
    :param sentence: a sentence str
    :return: a list of words which have been lemmatized.
    >>> lemmatization = Lemmatization()
    >>> lemmatization.lemmatize_sentence("I am running in a race.")
    ['I', 'be', 'run', 'in', 'a', 'race']

    """
    # Remove punctuation
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Get POS tags
    pos_tags = nltk.pos_tag(tokens)
    
    # Initialize lemmatizer
    lemmatizer = WordNetLemmatizer()
    
    # Helper function to convert NLTK POS tags to WordNet POS tags
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