import string

def remove_punctuation(self, sentence):
    """
    इनपुट टेक्स्ट से विराम चिह्न हटाता है।
    :param sentence: एक वाक्य str
    :return: str, बिना किसी विराम चिह्न के वाक्य
    >>> lemmatization = Lemmatization()
    >>> lemmatization.remove_punctuation("I am running in a race.")
    'I am running in a race'

    """
    return sentence.translate(str.maketrans('', '', string.punctuation))