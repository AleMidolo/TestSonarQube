def interpret(self, display=False):
    """
        संगीत स्कोर को व्याख्या करें जिसे खेला जाना है
        :param display: Bool, यह दर्शाता है कि व्याख्यायित स्कोर को प्रिंट करना है या नहीं
        :return: dict की सूची, dict में दो फ़ील्ड होते हैं, Chord और Tune, जो क्रमशः अक्षर और संख्या हैं। यदि इनपुट खाली है या केवल whitespace है, तो एक खाली सूची लौटाई जाती है।
        >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
        >>> play_list = context.interpret(display = False)
        [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]
        """
    if not self.play_text.strip():
        return []
    chords = []
    parts = self.play_text.split()
    for part in parts:
        chord = ''.join(filter(str.isalpha, part))
        tune = ''.join(filter(str.isdigit, part))
        chords.append({'Chord': chord, 'Tune': tune})
    if display:
        for chord in chords:
            print(self.display(chord['Chord'], chord['Tune']))
    return chords