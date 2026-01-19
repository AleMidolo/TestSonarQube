def vigenere_cipher(self, plaintext):
    """
        प्लेनटेक्स्ट को विजेनेरे सिफर का उपयोग करके एन्क्रिप्ट करता है।
        :param plaintext: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
        :return: ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
    ciphertext = ''
    key_length = len(self.key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
            else:
                ascii_offset = 97
            key_char = self.key[i % key_length]
            key_shift = ord(key_char.lower()) - 97
            shifted_char = chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext