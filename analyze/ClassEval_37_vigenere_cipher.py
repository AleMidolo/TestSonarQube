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
    key_length = len(self.key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = self.key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                ascii_offset = 65
            else:
                ascii_offset = 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext