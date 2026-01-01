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
    current_song_before_shuffle = self.current_song
    random.shuffle(self.playlist)
    if current_song_before_shuffle and current_song_before_shuffle in self.playlist:
        self.current_song = current_song_before_shuffle
    else:
        self.current_song = self.playlist[0] if self.playlist else None
    return True