def count_words(self, sentence):
    """
        एक वाक्य में शब्दों की संख्या गिनें। ध्यान दें कि शब्दों को स्पेस द्वारा अलग किया गया है और विराम चिह्न और संख्याएँ शब्दों के रूप में नहीं गिनी जाती हैं।
        :param sentence:string, गिनने के लिए वाक्य, जहाँ शब्द स्पेस द्वारा अलग किए गए हैं
        :return:int, वाक्य में शब्दों की संख्या
        >>> ss.count_words("abc def")
        2
        """
    cleaned = re.sub('[^\\w\\s]', '', sentence)
    cleaned = re.sub('\\d+', '', cleaned)
    words = cleaned.split()
    return len([word for word in words if word.strip()])