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
    key_as_int = [ord(i) - 97 for i in self.key.lower()]
    plaintext_int = [ord(i) - 97 for i in plaintext.lower()]
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 97)
    return ciphertext