def split_sentences(self, sentences_string):
    """
    एक स्ट्रिंग को वाक्यों की सूची में विभाजित करें। वाक्य . या ? के साथ समाप्त होते हैं और उसके बाद एक स्पेस होता है। कृपया ध्यान दें कि Mr. भी . के साथ समाप्त होता है लेकिन ये वाक्य नहीं हैं।
    :param sentences_string: स्ट्रिंग, विभाजित करने के लिए स्ट्रिंग
    :return: सूची, विभाजित वाक्य सूची
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    import re
    
    # Pattern to match sentences ending with . or ? followed by space or end of string
    # Negative lookbehind to avoid splitting on abbreviations like "Mr."
    pattern = r'(?<!\bMr)(?<!\bMrs)(?<!\bDr)(?<!\bMs)(?<!\bProf)[.?](?=\s|$)'
    
    # Split by the pattern
    parts = re.split(pattern, sentences_string)
    
    # Reconstruct sentences with their punctuation
    sentences = []
    current_pos = 0
    
    for match in re.finditer(pattern, sentences_string):
        end_pos = match.end() - 1  # Position of . or ?
        sentence = sentences_string[current_pos:end_pos + 1].strip()
        if sentence:
            sentences.append(sentence)
        current_pos = match.end()
    
    # Add any remaining text
    if current_pos < len(sentences_string):
        remaining = sentences_string[current_pos:].strip()
        if remaining:
            sentences.append(remaining)
    
    return sentences