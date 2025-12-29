def vigenere_decipher(self, ciphertext):
    """
        Decifra il testo cifrato fornito utilizzando il cifrario di Vigenere
        :param ciphertext: Il testo cifrato da decifrare, str.
        :return: Il testo in chiaro decifrato, str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
    key = self.key
    key_length = len(key)
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length].lower()) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            key_index += 1
        else:
            plaintext += char
    return plaintext