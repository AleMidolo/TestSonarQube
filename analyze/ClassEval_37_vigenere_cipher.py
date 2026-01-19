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
            is_upper = char.isupper()
            plain_char_num = ord(char.lower()) - ord('a')
            key_char_num = ord(key_repeated[i].lower()) - ord('a')
            encrypted_num = (plain_char_num + key_char_num) % 26
            encrypted_char = chr(encrypted_num + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext