def vigenere_decipher(self, ciphertext):
    """
        दिए गए ciphertext को Vigenere cipher का उपयोग करके डिकोड करता है
        :param ciphertext: डिकोड करने के लिए ciphertext, str.
        :return: डिकोड किया गया plaintext, str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
    plaintext = ''
    key_length = len(self.key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = self.key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                ascii_offset = 65
                base_char = key_char.upper()
            else:
                ascii_offset = 97
                base_char = key_char.lower()
            decrypted_char = chr((ord(char) - ascii_offset - (ord(base_char) - ascii_offset)) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext