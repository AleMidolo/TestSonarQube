def remove_song(self, song):
    """
    Removes a song from the playlist.
    :param song: The song to remove from the playlist, str.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.remove_song("song1")
    >>> musicPlayer.playlist
    ['song2']

    """
    if song in self.playlist:
        self.playlist.remove(song)