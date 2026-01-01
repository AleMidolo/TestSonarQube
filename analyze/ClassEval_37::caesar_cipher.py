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
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text