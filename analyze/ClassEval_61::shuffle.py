def shuffle(self):
    """
        随机打乱播放列表。
        :return: 如果播放列表被打乱则返回 True，如果播放列表为空则返回 False。
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.shuffle()
        True

        """
    if not self.playlist:
        return False
    random.shuffle(self.playlist)
    if self.current_song and self.current_song in self.playlist:
        current_index = self.playlist.index(self.current_song)
        self.current_song = self.playlist[current_index]
    return True