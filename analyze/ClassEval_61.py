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
            self._stop_if_current_song(song)

    def _stop_if_current_song(self, song):
        if self.current_song == song:
            self.stop()

    def play(self):
        if self._has_songs():
            return self.playlist[0]
        return False

    def _has_songs(self):
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
        if self.MIN_VOLUME <= volume <= self.MAX_VOLUME:
            self.volume = volume
            return True
        return False

    def shuffle(self):
        if self.playlist:
            import random
            random.shuffle(self.playlist)
            return True
        return False

    def _is_playlist_empty(self):
        return not self.playlist