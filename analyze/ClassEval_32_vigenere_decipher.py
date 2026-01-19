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
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
                key_char = self.key[key_index % key_length].upper()
            else:
                ascii_offset = 97
                key_char = self.key[key_index % key_length].lower()
            key_shift = ord(key_char) - ascii_offset
            decrypted_char = chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext