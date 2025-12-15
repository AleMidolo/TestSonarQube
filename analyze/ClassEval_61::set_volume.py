def set_volume(self, volume):
        """
        संगीत प्लेयर की मात्रा सेट करता है, यदि मात्रा 0 और 100 के बीच है तो यह मान्य है।
        :param volume: संगीत प्लेयर के लिए सेट करने के लिए मात्रा, int।
        :return: यदि मात्रा सेट की गई थी तो True, यदि मात्रा अमान्य थी तो False।
        >>> musicPlayer = MusicPlayer()
        >>> musicPlayer.set_volume(50)
        >>> musicPlayer.volume
        50

        """
        if 0 <= volume <= 100:
            self.volume = volume
            return True
        return False