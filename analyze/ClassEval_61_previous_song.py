def previous_song(self):
    """
    切换到播放列表中的上一首歌曲。
    :return: 如果切换到了上一首歌曲则返回 True，如果没有上一首歌曲则返回 False。
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.current_song = "song2"
    >>> musicPlayer.previous_song()
    True

    """
    if not hasattr(self, 'playlist') or not self.playlist:
        return False
    
    if not hasattr(self, 'current_song') or self.current_song is None:
        return False
    
    try:
        current_index = self.playlist.index(self.current_song)
        if current_index > 0:
            self.current_song = self.playlist[current_index - 1]
            return True
        else:
            return False
    except ValueError:
        return False