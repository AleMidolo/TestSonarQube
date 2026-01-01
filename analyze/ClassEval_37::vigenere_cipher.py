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
            plaintext_offset = ord('A') if char.isupper() else ord('a')
            key_char = key_repeated[i % len(key_repeated)]
            key_offset = ord('A') if key_char.isupper() else ord('a')
            key_shift = ord(key_char) - key_offset
            shifted_char = chr((ord(char) - plaintext_offset + key_shift) % 26 + plaintext_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext