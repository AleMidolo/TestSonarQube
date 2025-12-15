class AutomaticGuitarSimulator: 
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text

    def interpret(self, display=False):
        """
        Interpret the music score to be played
        :param display:Bool, representing whether to print the interpreted score
        :return: list of dict, The dict includes two fields, Chord and Tune, which are letters and numbers, respectively. If the input is empty or contains only whitespace, an empty list is returned.
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
        if not self.play_text.strip():
            return []
        else:
            play_list = []
            play_segs = self.play_text.split(" ")
            for play_seg in play_segs:
                pos = 0
                for ele in play_seg:
                    if ele.isalpha():
                        pos += 1
                        continue
                    break
                play_chord = play_seg[0:pos]
                play_value = play_seg[pos:]
                play_list.append({'Chord': play_chord, 'Tune': play_value})
                if display:
                    self.display(play_chord, play_value)
            return play_list

    def display(self, key, value):
        """
        निम्नलिखित प्रारूप के साथ कॉर्ड प्रिंट करें और धुन बजाएं: सामान्य गिटार खेलने का तरीका -- कॉर्ड: %s, धुन बजाएं: %s
        :param key:str, कॉर्ड
        :param value:str, धुन बजाएं
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        सामान्य गिटार खेलने का तरीका -- कॉर्ड: C, धुन बजाएं: 53231323
        """
        print("सामान्य गिटार खेलने का तरीका -- कॉर्ड: %s, धुन बजाएं: %s" % (key, value))