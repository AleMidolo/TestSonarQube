def lemmatize_sentence(self, sentence):
    """
    移除句子中的标点符号并对输入句子进行分词，为每个单词标记词性标签，
    根据它们的词性对单词进行词形还原，并将结果存储在一个列表中。
    :param sentence: 一个句子，str
    :return: 一个已进行词形还原的单词列表。
    >>> lemmatization = Lemmatization()
    >>> lemmatization.lemmatize_sentence("I am running in a race.")
    ['I', 'be', 'run', 'in', 'a', 'race']
    """
    sentence = self.remove_punctuation(sentence)
    words = word_tokenize(sentence)
    pos_tags = self.get_pos_tag(sentence)
    lemmatized_words = [self.lemmatizer.lemmatize(word, pos=self.get_wordnet_pos(pos)) for word, pos in zip(words, pos_tags)]
    return lemmatized_words

def get_wordnet_pos(self, pos):
    """
    Convert POS tag to WordNet format.
    :param pos: str, part of speech tag
    :return: str, corresponding WordNet POS tag
    """
    if pos.startswith('J'):
        return 'a'  # adjective
    elif pos.startswith('V'):
        return 'v'  # verb
    elif pos.startswith('N'):
        return 'n'  # noun
    elif pos.startswith('R'):
        return 'r'  # adverb
    else:
        return 'n'  # default to noun