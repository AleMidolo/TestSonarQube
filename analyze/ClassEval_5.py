class AutomaticGuitarSimulator:
    def __init__(self, text) -> None:
        self.play_text = text

    def interpret(self, display=False):
        if not self._has_play_text():
            return []
        
        play_list = []
        play_segs = self.play_text.split(" ")
        for play_seg in play_segs:
            play_chord, play_value = self._extract_chord_and_value(play_seg)
            play_list.append({'Chord': play_chord, 'Tune': play_value})
            if display:
                self.display(play_chord, play_value)
        return play_list

    def _has_play_text(self):
        return bool(self.play_text.strip())

    def _extract_chord_and_value(self, play_seg):
        pos = self._find_chord_length(play_seg)
        play_chord = play_seg[0:pos]
        play_value = play_seg[pos:]
        return play_chord, play_value

    def _find_chord_length(self, play_seg):
        pos = 0
        for ele in play_seg:
            if ele.isalpha():
                pos += 1
                continue
            break
        return pos

    def display(self, key, value):
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value)