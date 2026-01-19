def shuffle(self):
    """
        Mescola l'ordine della playlist.
        :return: True se la playlist è stata mescolata, False se la playlist era vuota.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["canzone1", "canzone2"]
        >>> musicPlayer.shuffle()
        True

        """
    if not self.playlist:
        return False
    random.shuffle(self.playlist)
    if self.current_song and self.current_song in self.playlist:
        current_index = self.playlist.index(self.current_song)
        self.current_song = self.playlist[current_index]
    return True