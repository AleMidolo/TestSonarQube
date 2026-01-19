def count_words(self, sentence):
    """
        एक वाक्य में शब्दों की संख्या गिनें। ध्यान दें कि शब्दों को स्पेस द्वारा अलग किया गया है और विराम चिह्न और संख्याएँ शब्दों के रूप में नहीं गिनी जाती हैं।
        :param sentence:string, गिनने के लिए वाक्य, जहाँ शब्द स्पेस द्वारा अलग किए गए हैं
        :return:int, वाक्य में शब्दों की संख्या
        >>> ss.count_words("abc def")
        2
        """
    tokens = sentence.split()
    word_count = 0
    for token in tokens:
        cleaned_token = re.sub('[^\\w\\s]', '', token)
        if re.search('[a-zA-Z]', cleaned_token):
            word_count += 1
    return word_count