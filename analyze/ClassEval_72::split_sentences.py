def split_sentences(self, text):
    """
        पाठ को वाक्यों की सूची में विभाजित करें बिना विराम चिह्न के, अंतिम वाक्य को छोड़कर
        :param text: विभाजित करने के लिए पाठ
        :return: विभाजित पाठ सूची
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
    pattern = self.generate_split_sentences_pattern()
    parts = re.split(pattern, text)
    result = []
    for i, part in enumerate(parts):
        if i < len(parts) - 1:
            result.append(part.rstrip('.!?'))
        else:
            result.append(part)
    return result