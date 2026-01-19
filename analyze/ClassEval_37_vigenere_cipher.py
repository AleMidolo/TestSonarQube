def vigenere_cipher(self, plaintext):
    """
        使用维吉尼亚密码加密明文。
        :param plaintext: 要加密的明文，str。
        :return: 密文，str。
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
                base_char = char
            else:
                ascii_offset = 97
                base_char = char
            shifted_char = chr((ord(base_char) - ascii_offset + key_shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext