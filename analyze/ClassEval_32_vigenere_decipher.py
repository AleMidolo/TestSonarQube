def vigenere_decipher(self, ciphertext):
    """
        使用维吉尼亚密码解密给定的密文
        :param ciphertext: 要解密的密文，str。
        :return: 解密后的明文，str。
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'

        """
    plaintext = ''
    key_length = len(self.key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = self.key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                ascii_offset = 65
                base_char = key_char.upper()
            else:
                ascii_offset = 97
                base_char = key_char.lower()
            shifted_char = chr((ord(char) - ascii_offset - key_shift) % 26 + ascii_offset)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext