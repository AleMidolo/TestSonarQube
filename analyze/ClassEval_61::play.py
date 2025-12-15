def play(self):
        """
        播放播放列表中的当前歌曲。
        :return: 播放列表中的当前歌曲，如果没有当前歌曲则返回 False。
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.play()
        'song1'
        """
        if self.current_song:
            return self.current_song
        else:
            return False