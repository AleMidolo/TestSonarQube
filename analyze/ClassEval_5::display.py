def display(self, key, value):
    """
        Imprime el acorde y toca la melodía con el siguiente formato: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, acorde
        :param value:str, tocar melodía
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323
        """
    print(f'Normal Guitar Playing -- Chord: {key}, Play Tune: {value}')