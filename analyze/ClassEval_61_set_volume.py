def set_volume(self, volume):
    """
    设置音乐播放器的音量，如果音量在0到100之间则有效。
    :param volume: 要设置的音乐播放器音量，int类型。
    :return: 如果音量设置成功则返回True，如果音量无效则返回False。
    >>> musicPlayer = MusicPlayer()
    >>> musicPlayer.set_volume(50)
    >>> musicPlayer.volume
    50

    """
    if 0 <= volume <= 100:
        self.volume = volume
        return True
    else:
        return False