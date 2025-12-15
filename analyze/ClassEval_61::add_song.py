def add_song(self, song):
    """
    प्लेलिस्ट में एक गाना जोड़ता है।
    :param song: प्लेलिस्ट में जोड़ने के लिए गाना, str.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.add_song("song1")
    >>> musicPlayer.playlist
    ['song1']

    """
    self.playlist.append(song)