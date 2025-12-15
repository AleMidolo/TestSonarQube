def switch_song(self):
        """
        प्लेलिस्ट में अगले गाने पर स्विच करता है।
        :return: यदि अगले गाने पर स्विच किया गया, तो True, यदि कोई अगला गाना नहीं है, तो False।
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["song1", "song2"]
        >>> musicPlayer.current_song = "song1"
        >>> musicPlayer.switch_song()
        True

        """
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            if current_index < len(self.playlist) - 1:
                self.current_song = self.playlist[current_index + 1]
                return True
            else:
                return False
        else:
            return False