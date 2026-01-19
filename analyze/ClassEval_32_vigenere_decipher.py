def vigenere_decipher(self, ciphertext):
    """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
    plaintext = ''
    key_repeated = (self.key * (len(ciphertext) // len(self.key) + 1))[:len(ciphertext)]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = key_repeated[i]
            key_shift = ord(key_char.lower()) - 97
            if char.isupper():
                ascii_offset = 65
                plain_char = chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
            else:
                ascii_offset = 97
                plain_char = chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
            plaintext += plain_char
        else:
            plaintext += char
    return plaintext