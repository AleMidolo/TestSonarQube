def previous_song(self):
        """
        Passa alla canzone precedente nella playlist.
        :return: True se è stata cambiata la canzone precedente, False se non c'era una canzone precedente.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["canzone1", "canzone2"]
        >>> musicPlayer.current_song = "canzone2"
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