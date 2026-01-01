def shuffle(self):
    """
        Mezcla la lista de reproducción.
        :return: True si la lista de reproducción fue mezclada, False si la lista de reproducción estaba vacía.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["canción1", "canción2"]
        >>> musicPlayer.shuffle()
        True

        """
    if not self.playlist:
        return False
    current_song_before_shuffle = self.current_song
    random.shuffle(self.playlist)
    if current_song_before_shuffle and current_song_before_shuffle in self.playlist:
        self.current_song = current_song_before_shuffle
    return True