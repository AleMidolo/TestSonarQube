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