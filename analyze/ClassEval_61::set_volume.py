def set_volume(self, volume):
    """
        Imposta il volume del lettore musicale, se il volume è compreso tra 0 e 100 è valido.
        :param volume: Il volume da impostare per il lettore musicale, int.
        :return: True se il volume è stato impostato, False se il volume non era valido.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.set_volume(50)
        >>> musicPlayer.volume
        50

        """
    if 0 <= volume <= 100:
        self.volume = volume
        return True
    else:
        return False