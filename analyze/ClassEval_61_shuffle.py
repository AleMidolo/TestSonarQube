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
    current_song_before_shuffle = self.current_song
    random.shuffle(self.playlist)
    if current_song_before_shuffle and current_song_before_shuffle in self.playlist:
        self.current_song = current_song_before_shuffle
    else:
        self.current_song = self.playlist[0] if self.playlist else None
    return True