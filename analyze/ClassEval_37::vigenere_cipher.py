def vigenere_cipher(self, plaintext):
    """
        Encrypts the plaintext using the Vigenere cipher.
        :param plaintext: The plaintext to encrypt, str.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
    ciphertext = ''
    key_repeated = (self.key * (len(plaintext) // len(self.key) + 1))[:len(plaintext)]
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = key_repeated[i]
            key_shift = ord(key_char.lower()) - 97
            if char.isupper():
                ascii_offset = 65
                base_char = char
            else:
                ascii_offset = 97
                base_char = char
            shifted_char = chr((ord(base_char) - ascii_offset + key_shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext