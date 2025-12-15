def previous_song(self):
        """
        प्लेलिस्ट में पिछले गाने पर स्विच करता है।
        :return: यदि पिछले गाने पर स्विच किया गया है तो True, यदि कोई पिछला गाना नहीं था तो False।
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song2"
        >>> musicPlayer.previous_song()
        True

        """
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            if current_index > 0:
                self.current_song = self.playlist[current_index - 1]
                return True
            else:
                return False
        else:
            return False