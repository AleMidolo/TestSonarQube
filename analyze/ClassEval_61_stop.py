def stop(self):
    """
    प्लेलिस्ट में वर्तमान गीत को रोकता है।
    :return: यदि वर्तमान गीत रोका गया है तो True, यदि कोई वर्तमान गीत नहीं था तो False।
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.current_song = "song1"
    >>> musicPlayer.stop()
    True

    """
    if self.current_song is not None:
        self.current_song = None
        return True
    return False