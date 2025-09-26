class MusicPlayer:
    MAX_VOLUME = 100
    MIN_VOLUME = 0

    def __init__(self):
        self.playlist = []
        self.current_song = None
        self.volume = 50

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            self.stop_if_current_song(song)

    def stop_if_current_song(self, song):
        if self.current_song == song:
            self.stop()

    def play(self):
        if self.has_songs():
            return self.playlist[0]
        return False

    def has_songs(self):
        return bool(self.playlist) and self.current_song is not None

    def stop(self):
        if self.current_song:
            self.current_song = None
            return True
        return False

    def switch_song(self):
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            if current_index < len(self.playlist) - 1:
                self.current_song = self.playlist[current_index + 1]
                return True
        return False

    def previous_song(self):
        if self.current_song:
            current_index = self.playlist.index(self.current_song)
            if current_index > 0:
                self.current_song = self.playlist[current_index - 1]
                return True
        return False

    def set_volume(self, volume):
        if self.is_volume_valid(volume):
            self.volume = volume
        return False

    def is_volume_valid(self, volume):
        return self.MIN_VOLUME <= volume <= self.MAX_VOLUME

    def shuffle(self):
        if self.playlist:
            import random
            random.shuffle(self.playlist)
            return True
        return False

    def has_current_song(self):
        return self.current_song is not None