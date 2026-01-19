def shuffle(self):
    """
        प्लेलिस्ट को शफल करता है।
        :return: यदि प्लेलिस्ट शफल की गई है तो True, यदि प्लेलिस्ट खाली है तो False।
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