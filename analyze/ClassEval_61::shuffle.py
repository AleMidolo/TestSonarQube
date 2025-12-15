def shuffle(self):
        """
        Mescola l'ordine della playlist.
        :return: True se la playlist è stata mescolata, False se la playlist era vuota.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["canzone1", "canzone2"]
        >>> musicPlayer.shuffle()
        True

        """
        if self.playlist:
            random.shuffle(self.playlist)
            return True
        return False