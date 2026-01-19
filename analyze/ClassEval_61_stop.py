def stop(self):
    """
    Detiene la canción actual en la lista de reproducción.
    :return: True si la canción actual fue detenida, False si no había ninguna canción actual.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["canción1", "canción2"]
    >>> musicPlayer.current_song = "canción1"
    >>> musicPlayer.stop()
    True

    """
    if self.current_song is not None:
        self.current_song = None
        return True
    return False