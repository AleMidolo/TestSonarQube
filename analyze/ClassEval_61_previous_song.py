def previous_song(self):
    """
    Switches to the previous song in the playlist.
    :return: True if the previous song was switched to, False if there was no previous song.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.current_song = "song2"
    >>> musicPlayer.previous_song()
    True

    """
    if not self.playlist or self.current_song not in self.playlist:
        return False
    
    current_index = self.playlist.index(self.current_song)
    
    if current_index > 0:
        self.current_song = self.playlist[current_index - 1]
        return True
    else:
        return False