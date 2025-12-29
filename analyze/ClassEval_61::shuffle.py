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
    random.shuffle(self.playlist)
    if self.current_song and self.current_song in self.playlist:
        current_index = self.playlist.index(self.current_song)
        self.playlist.pop(current_index)
        self.playlist.insert(0, self.current_song)
    return True