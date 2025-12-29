def vigenere_cipher(self, plaintext):
    """
        प्लेनटेक्स्ट को विजेनेरे सिफर का उपयोग करके एन्क्रिप्ट करता है।
        :param plaintext: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
        :return: ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
    key = self.key
    key_length = len(key)
    plaintext_length = len(plaintext)
    ciphertext = ''
    for i in range(plaintext_length):
        if plaintext[i].isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if plaintext[i].isupper():
                ciphertext += chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(plaintext[i]) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += plaintext[i]
    return ciphertext