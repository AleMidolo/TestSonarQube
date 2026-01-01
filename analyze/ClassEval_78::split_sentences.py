def split_sentences(self, sentences_string):
    """
        Suddivide una stringa in una lista di frasi. Le frasi terminano con . o ? e con uno spazio dopo. Si prega di notare che Mr. termina anch'esso con . ma non è una frase.
        :param sentences_string: stringa, stringa da suddividere
        :return: lista, lista delle frasi suddivise
        >>> ss = SplitSentence()
        >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
        ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
        """
    return re.split('(?<=[.?\\s])\\s*', sentences_string.strip())