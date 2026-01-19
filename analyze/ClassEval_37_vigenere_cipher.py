def vigenere_cipher(self, plaintext):
    """
        Cifra el texto plano utilizando el cifrado de Vigenere.
        :param plaintext: El texto plano a encriptar, str.
        :return: El texto cifrado, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
    ciphertext = ''
    key_length = len(self.key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = self.key[i % key_length]
            key_shift = ord(key_char.lower()) - 97
            if char.isupper():
                ascii_offset = 65
            else:
                ascii_offset = 97
            shifted_char = chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext