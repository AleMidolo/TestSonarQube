import random

def shuffle(self):
    """
    Mezcla la lista de reproducción.
    :return: True si la lista de reproducción fue mezclada, False si la lista de reproducción estaba vacía.
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["canción1", "canción2"]
    >>> musicPlayer.shuffle()
    True

    """
    if not self.playlist:
        return False
    
    random.shuffle(self.playlist)
    return True