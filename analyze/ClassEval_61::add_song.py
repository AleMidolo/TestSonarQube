def add_song(self, song):
    """
        प्लेलिस्ट में एक गाना जोड़ता है।
        :param song: प्लेलिस्ट में जोड़ने के लिए गाना, str.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.add_song("song1")
        >>> musicPlayer.playlist
        ['song1']
        """
    if song and isinstance(song, str):
        self.playlist.append(song)
        if self.current_song is None and len(self.playlist) == 1:
            self.current_song = song