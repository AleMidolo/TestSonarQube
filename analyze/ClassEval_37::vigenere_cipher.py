def vigenere_cipher(self, plaintext):
    """
        Cripta il testo in chiaro utilizzando il cifrario di Vigenere.
        :param plaintext: Il testo in chiaro da criptare, str.
        :return: Il testo cifrato, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'

        """
    ciphertext = ''
    key_repeated = (self.key * (len(plaintext) // len(self.key) + 1))[:len(plaintext)]
    for i in range(len(plaintext)):
        plain_char = plaintext[i]
        key_char = key_repeated[i]
        if plain_char.isalpha():
            plain_offset = 65 if plain_char.isupper() else 97
            key_offset = 65 if key_char.isupper() else 97
            plain_num = ord(plain_char) - plain_offset
            key_num = ord(key_char) - key_offset
            encrypted_num = (plain_num + key_num) % 26
            encrypted_char = chr(encrypted_num + plain_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += plain_char
    return ciphertext