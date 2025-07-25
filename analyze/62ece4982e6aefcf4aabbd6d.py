from typing import List

def string_to_int(string: str, alphabet: List[str]) -> int:
    """
    एक स्ट्रिंग को एक संख्या में बदलने का कार्य करता है, दिए गए वर्णमाला का उपयोग करके।

    इनपुट यह मानता है कि सबसे महत्वपूर्ण अंक (most significant digit) पहले है।
    """
    base = len(alphabet)
    value = 0
    for char in string:
        value = value * base + alphabet.index(char)
    return value