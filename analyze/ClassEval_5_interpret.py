def interpret(self, display=False):
    """
    संगीत स्कोर को व्याख्या करें जिसे खेला जाना है
    :param display: Bool, यह दर्शाता है कि व्याख्यायित स्कोर को प्रिंट करना है या नहीं
    :return: dict की सूची, dict में दो फ़ील्ड होते हैं, Chord और Tune, जो क्रमशः अक्षर और संख्या हैं। यदि इनपुट खाली है या केवल whitespace है, तो एक खाली सूची लौटाई जाती है।
    >>> context = AutomaticGuitarSimulator("C53231323 Em43231323 F43231323 G63231323")
    >>> play_list = context.interpret(display = False)
    [{'Chord': 'C', 'Tune': '53231323'}, {'Chord': 'Em', 'Tune': '43231323'}, {'Chord': 'F', 'Tune': '43231323'}, {'Chord': 'G', 'Tune': '63231323'}]

    """
    # Check if the input score is empty or only whitespace
    if not hasattr(self, 'score') or not self.score or not self.score.strip():
        return []
    
    # Split the score by whitespace to get individual chord-tune pairs
    tokens = self.score.split()
    
    play_list = []
    
    for token in tokens:
        if not token:
            continue
        
        # Separate chord (letters) from tune (numbers)
        chord = ""
        tune = ""
        
        for char in token:
            if char.isalpha():
                chord += char
            elif char.isdigit():
                tune += char
        
        # Only add if both chord and tune exist
        if chord and tune:
            play_list.append({'Chord': chord, 'Tune': tune})
    
    # Display if requested
    if display:
        print(play_list)
    
    return play_list