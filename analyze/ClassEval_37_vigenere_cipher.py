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
            is_upper = char.isupper()
            plain_char = char.lower()
            key_char = key_repeated[i % len(key_repeated)].lower()
            plain_num = ord(plain_char) - ord('a')
            key_num = ord(key_char) - ord('a')
            encrypted_num = (plain_num + key_num) % 26
            encrypted_char = chr(encrypted_num + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext