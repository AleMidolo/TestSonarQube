def split_sentences(self, text):
        """
        Suddivide il testo in un elenco di frasi senza punteggiatura tranne l'ultima frase
        :param text: Testo da suddividere
        :return: Elenco di testo suddiviso
        >>> ru = RegexUtils()
        >>> ru.split_sentences("Aaa. Bbbb? Ccc!")
        ['Aaa', 'Bbbb', 'Ccc!']
        """
        pattern = self.generate_split_sentences_pattern()
        sentences = re.split(pattern, text)
        return [sentence.strip() for sentence in sentences if sentence]