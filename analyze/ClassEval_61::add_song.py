def add_song(self, song):
    """
    Adds a song to the playlist.
    :param song: The song to add to the playlist, str.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.add_song("song1")
    >>> musicPlayer.playlist
    ['song1']

    """
    self.playlist.append(song)