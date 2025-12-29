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