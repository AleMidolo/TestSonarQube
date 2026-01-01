def shuffle(self):
    """
        Shuffles the playlist.
        :return: True if the playlist was shuffled, False if the playlist was empty.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
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