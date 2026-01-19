def shuffle(self):
    """
    प्लेलिस्ट को शफल करता है।
    :return: यदि प्लेलिस्ट शफल की गई है तो True, यदि प्लेलिस्ट खाली है तो False।
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.playlist = ["song1", "song2"]
    >>> musicPlayer.shuffle()
    True

    """
    import random
    
    if not self.playlist:
        return False
    
    random.shuffle(self.playlist)
    return True