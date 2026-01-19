def switch_song(self):
    """
    Switches to the next song in the playlist.
    :return: True if the next song was switched to, False if there was no next song.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.current_song = "song1"
    >>> musicPlayer.switch_song()
    True

    """
    if not self.playlist:
        return False
    
    if self.current_song is None:
        return False
    
    try:
        current_index = self.playlist.index(self.current_song)
        next_index = current_index + 1
        
        if next_index < len(self.playlist):
            self.current_song = self.playlist[next_index]
            return True
        else:
            return False
    except ValueError:
        # current_song is not in playlist
        return False