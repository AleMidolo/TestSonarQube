def previous_song(self):
    """
    Passa alla canzone precedente nella playlist.
    :return: True se è stata cambiata la canzone precedente, False se non c'era una canzone precedente.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["canzone1", "canzone2"]
    >>> musicPlayer.current_song = "canzone2"
    >>> musicPlayer.previous_song()
    True

    """
    if not self.playlist or self.current_song is None:
        return False
    
    try:
        current_index = self.playlist.index(self.current_song)
        if current_index > 0:
            self.current_song = self.playlist[current_index - 1]
            return True
        else:
            return False
    except ValueError:
        return False