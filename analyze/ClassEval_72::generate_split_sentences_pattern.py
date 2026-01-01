def generate_split_sentences_pattern(self):
    """
        Genera patterns di espressione regolare che corrispondono ai caratteri centrali di due frasi
        :return: stringa, modelli di espressione regolare che corrispondono ai caratteri centrali di due frasi
        >>> ru = RegexUtils()
        >>> ru.generate_split_sentences_pattern()
        '[.!?][\\s]{1,2}(?=[A-Z])'
        """
    pattern = '[.!?][\\s]{1,2}(?=[A-Z])'
    return pattern