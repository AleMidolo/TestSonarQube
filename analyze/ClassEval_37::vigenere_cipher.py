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
            if char.isupper():
                ascii_offset = 65
                key_char = self.key[i % key_length].upper()
            else:
                ascii_offset = 97
                key_char = self.key[i % key_length].lower()
            if key_char.isalpha():
                key_shift = ord(key_char) - (65 if key_char.isupper() else 97)
                shifted_char = chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
                ciphertext += shifted_char
            else:
                ciphertext += char
        else:
            ciphertext += char
    return ciphertext