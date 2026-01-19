def switch_song(self):
    """
    प्लेलिस्ट में अगले गाने पर स्विच करता है।
    :return: यदि अगले गाने पर स्विच किया गया, तो True, यदि कोई अगला गाना नहीं है, तो False।
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.current_song = "song1"
    >>> musicPlayer.switch_song()
    True

    """
    if not hasattr(self, 'playlist') or not self.playlist:
        return False
    
    if not hasattr(self, 'current_song') or self.current_song is None:
        return False
    
    try:
        current_index = self.playlist.index(self.current_song)
        if current_index < len(self.playlist) - 1:
            self.current_song = self.playlist[current_index + 1]
            return True
        else:
            return False
    except ValueError:
        return False