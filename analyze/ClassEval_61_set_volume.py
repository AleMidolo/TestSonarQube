def set_volume(self, volume):
    """
        Establece el volumen del reproductor de música, si el volumen está entre 0 y 100 es válido.
        :param volume: El volumen para establecer en el reproductor de música, int.
        :return: True si el volumen fue establecido, False si el volumen era inválido.
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