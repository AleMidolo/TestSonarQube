def split_sentences(self, sentences_string):
    """
    एक स्ट्रिंग को वाक्यों की सूची में विभाजित करें। वाक्य . या ? के साथ समाप्त होते हैं और उसके बाद एक स्पेस होता है। कृपया ध्यान दें कि Mr. भी . के साथ समाप्त होता है लेकिन ये वाक्य नहीं हैं।
    :param sentences_string: स्ट्रिंग, विभाजित करने के लिए स्ट्रिंग
    :return: सूची, विभाजित वाक्य सूची
    >>> ss = SplitSentence()
    >>> ss.split_sentences("aaa aaaa. bb bbbb bbb? cccc cccc. dd ddd?")
    ['aaa aaaa.', 'bb bbbb bbb?', 'cccc cccc.', 'dd ddd?']
    """
    if not sentences_string:
        return []
    
    sentences = []
    current_sentence = ""
    i = 0
    
    while i < len(sentences_string):
        current_sentence += sentences_string[i]
        
        # Check if current character is . or ?
        if sentences_string[i] in '.?':
            # Check if this is followed by a space (or end of string)
            if i + 1 < len(sentences_string) and sentences_string[i + 1] == ' ':
                # Check if this is not "Mr." pattern
                # Mr. has pattern: capital letter + lowercase letters + .
                is_abbreviation = False
                if sentences_string[i] == '.':
                    # Look back to check for common abbreviations like Mr., Mrs., Dr., etc.
                    words = current_sentence.strip().split()
                    if words:
                        last_word = words[-1]
                        # Check if last word is a common abbreviation
                        if last_word in ['Mr.', 'Mrs.', 'Ms.', 'Dr.', 'Prof.', 'Sr.', 'Jr.']:
                            is_abbreviation = True
                
                if not is_abbreviation:
                    sentences.append(current_sentence.strip())
                    current_sentence = ""
                    i += 1  # Skip the space after sentence ending
                    continue
            elif i + 1 == len(sentences_string):
                # End of string
                sentences.append(current_sentence.strip())
                current_sentence = ""
        
        i += 1
    
    # Add any remaining content
    if current_sentence.strip():
        sentences.append(current_sentence.strip())
    
    return sentences