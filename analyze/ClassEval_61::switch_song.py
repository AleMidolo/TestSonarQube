def switch_song(self):
    """
        Cambia a la siguiente canción en la lista de reproducción.
        :return: True si se cambió a la siguiente canción, False si no había una siguiente canción.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["canción1", "canción2"]
        >>> musicPlayer.current_song = "canción1"
        >>> musicPlayer.switch_song()
        True

        """
    if self.current_song and self.playlist:
        current_index = self.playlist.index(self.current_song)
        if current_index < len(self.playlist) - 1:
            self.current_song = self.playlist[current_index + 1]
            return True
        else:
            return False
    elif self.playlist:
        self.current_song = self.playlist[0]
        return True
    return False