def add_song(self, song):
    """
        Aggiunge una canzone alla playlist.
        :param song: La canzone da aggiungere alla playlist, str.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.add_song("song1")
        >>> musicPlayer.playlist
        ['song1']
        """
    self.playlist.append(song)