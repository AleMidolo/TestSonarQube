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
    key_repeated = (self.key * (len(plaintext) // len(self.key) + 1))[:len(plaintext)]
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
                key_offset = ord(key_repeated[i].upper()) - 65
            else:
                ascii_offset = 97
                key_offset = ord(key_repeated[i].lower()) - 97
            shifted_char = chr((ord(char) - ascii_offset + key_offset) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext