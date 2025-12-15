def play(self):
    """
    Riproduce la canzone attuale nella playlist.
    :return: La canzone attuale nella playlist, oppure False se non c'è nessuna canzone attuale.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["canzone1", "canzone2"]
    >>> musicPlayer.current_song = "canzone1"
    >>> musicPlayer.play()
    'canzone1'
    """
    
    if self.current_song:
        return self.current_song
    else:
        return False