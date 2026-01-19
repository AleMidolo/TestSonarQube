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
                base = ord('A')
            else:
                base = ord('a')
            encrypted_char = chr((ord(plaintext[i]) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += plaintext[i]
    return ciphertext