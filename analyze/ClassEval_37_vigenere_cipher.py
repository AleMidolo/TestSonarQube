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
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ascii_offset = 65
                key_char = self.key[key_index % key_length].upper()
            else:
                ascii_offset = 97
                key_char = self.key[key_index % key_length].lower()
            key_shift = ord(key_char) - ascii_offset
            shifted_char = chr((ord(char) - ascii_offset + key_shift) % 26 + ascii_offset)
            ciphertext += shifted_char
            key_index += 1
        else:
            ciphertext += char
    return ciphertext