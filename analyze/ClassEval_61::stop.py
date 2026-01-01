def stop(self):
    """
        停止播放当前播放列表中的歌曲。
        :return: 如果当前歌曲被停止则返回 True，如果没有当前歌曲则返回 False。
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.stop()
        True

        """
    if self.current_song:
        self.current_song = None
        return True
    return False