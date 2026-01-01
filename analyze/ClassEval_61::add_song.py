def add_song(self, song):
    """
    Agrega una canción a la lista de reproducción.
    :param song: La canción a agregar a la lista de reproducción, str.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.add_song("song1")
    >>> musicPlayer.playlist
    ['song1']
    """
    self.playlist.append(song)