def add_song(self, song):
    """
        将歌曲添加到播放列表中。
        :param song: 要添加到播放列表的歌曲，str。
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.add_song("song1")
        >>> musicPlayer.playlist
        ['song1']
        """
    if song and song not in self.playlist:
        self.playlist.append(song)