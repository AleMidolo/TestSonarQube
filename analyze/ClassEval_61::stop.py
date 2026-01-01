def stop(self):
    """
        Interrompe la canzone attuale nella playlist.
        :return: True se la canzone attuale è stata fermata, False se non c'era nessuna canzone attuale.
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.playlist = ["canzone1", "canzone2"]
        >>> musicPlayer.current_song = "canzone1"
        >>> musicPlayer.stop()
        True

        """
    if self.current_song:
        self.current_song = None
        return True
    else:
        return False