def remove_song(self, song):
    """
        Rimuove una canzone dalla playlist.
        :param song: La canzone da rimuovere dalla playlist, str.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.remove_song("song1")
        >>> musicPlayer.playlist
        ['song2']

        """
    if song in self.playlist:
        self.playlist.remove(song)
        if self.current_song == song:
            self.current_song = None
        return True
    return False