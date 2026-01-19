def switch_song(self):
    """
    切换到播放列表中的下一首歌曲。
    :return: 如果切换到下一首歌曲则返回 True，如果没有下一首歌曲则返回 False。
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.current_song = "song1"
    >>> musicPlayer.switch_song()
    True

    """
    if not self.playlist:
        return False
    
    if self.current_song is None:
        self.current_song = self.playlist[0]
        return True
    
    try:
        current_index = self.playlist.index(self.current_song)
        if current_index < len(self.playlist) - 1:
            self.current_song = self.playlist[current_index + 1]
            return True
        else:
            return False
    except ValueError:
        # current_song not in playlist
        return False