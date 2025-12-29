def vigenere_decipher(self, ciphertext):
    """
        Decifra il testo cifrato fornito utilizzando il cifrario di Vigenere
        :param ciphertext: Il testo cifrato da decifrare, str.
        :return: Il testo in chiaro decifrato, str.
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
                plaintext += chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
            else:
                ascii_offset = 97
                plaintext += chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
        else:
            plaintext += char
    return plaintext