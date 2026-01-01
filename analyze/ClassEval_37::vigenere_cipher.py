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
    key_repeated = (self.key * (len(plaintext) // len(self.key) + 1))[:len(plaintext)]
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
                key_offset = 65 if key_repeated[i].isupper() else 97
            else:
                ascii_offset = 97
                key_offset = 65 if key_repeated[i].isupper() else 97
            shift = ord(key_repeated[i]) - key_offset
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext