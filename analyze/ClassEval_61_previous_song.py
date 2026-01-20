def previous_song(self):
    """
    Cambia a la canción anterior en la lista de reproducción.
    :return: True si se cambió a la canción anterior, False si no había canción anterior.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["canción1", "canción2"]
    >>> musicPlayer.current_song = "canción2"
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