def vigenere_decipher(self, ciphertext):
    """
        दिए गए ciphertext को Vigenere cipher का उपयोग करके डिकोड करता है
        :param ciphertext: डिकोड करने के लिए ciphertext, str.
        :return: डिकोड किया गया plaintext, str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
    key_length = len(self.key)
    key_as_int = [ord(i) - ord('a') for i in self.key]
    ciphertext_int = [ord(i) - ord('a') for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + ord('a'))
    return plaintext