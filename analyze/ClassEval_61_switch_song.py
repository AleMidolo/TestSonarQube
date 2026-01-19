def switch_song(self):
    """
    Passa alla canzone successiva nella playlist.
    :return: True se la canzone successiva è stata cambiata, False se non c'era una canzone successiva.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["canzone1", "canzone2"]
    >>> musicPlayer.current_song = "canzone1"
    >>> musicPlayer.switch_song()
    True

    """
    if not self.playlist:
        return False
    
    if self.current_song is None:
        return False
    
    try:
        current_index = self.playlist.index(self.current_song)
        if current_index < len(self.playlist) - 1:
            self.current_song = self.playlist[current_index + 1]
            return True
        else:
            return False
    except ValueError:
        return False