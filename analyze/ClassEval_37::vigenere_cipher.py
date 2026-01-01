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
            key_char = key_repeated[i % len(key_repeated)]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                ascii_offset = 65
                base_char = key_char.upper()
            else:
                ascii_offset = 97
                base_char = key_char.lower()
            shifted_char = chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext