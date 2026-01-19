def caesar_cipher(self, plaintext, shift):
    """
    प्लेनटेक्स्ट को सीज़र सिफर का उपयोग करके एन्क्रिप्ट करता है।
    :param plaintext: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
    :param shift: प्लेनटेक्स्ट में प्रत्येक वर्ण को स्थानांतरित करने के लिए वर्णों की संख्या, int.
    :return: ciphertext, str.
    >>> e = EncryptionUtils("key")
    >>> e.caesar_cipher("abc", 1)
    'bcd'

    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    
    return ciphertext