class AutomaticGuitarSimulator: 
    def __init__(self, text) -> None:
        """
        Initialize the score to be played
        :param text:str, score to be played
        """
        self.play_text = text

    def display(self, key, value):
        """
        Print out chord and play tune with following format: Normal Guitar Playing -- Chord: %s, Play Tune: %s
        :param key:str, chord
        :param value:str, play tune
        :return: str
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> context.display("C", "53231323")
        Normal Guitar Playing -- Chord: C, Play Tune: 53231323
        """
        return "Normal Guitar Playing -- Chord: %s, Play Tune: %s" % (key, value)

    def interpret(self, display=False):
        """
        解析要演奏的乐谱
        :param display: Bool，表示是否打印解析后的乐谱
        :return: dict 的列表，字典包括两个字段，Chord 和 Tune，分别是字母和数字。如果输入为空或仅包含空格，则返回一个空列表。
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
        if not self.play_text.strip():
            return []
        
        chords_and_tunes = []
        parts = self.play_text.split()
        
        for part in parts:
            chord = ''.join(filter(str.isalpha, part))
            tune = ''.join(filter(str.isdigit, part))
            chords_and_tunes.append({'Chord': chord, 'Tune': tune})
        
        if display:
            for item in chords_and_tunes:
                print(self.display(item['Chord'], item['Tune']))
        
        return chords_and_tunes