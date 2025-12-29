def remove_song(self, song):
    """
        从播放列表中移除一首歌曲。
        :param song: 要从播放列表中移除的歌曲，str。
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