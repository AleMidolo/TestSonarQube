def remove_song(self, song):
    """
        प्लेलिस्ट से एक गाना हटाता है।
        :param song: प्लेलिस्ट से हटाने के लिए गाना, str.
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