def vigenere_decipher(self, ciphertext):
    """
        使用维吉尼亚密码解密给定的密文
        :param ciphertext: 要解密的密文，str。
        :return: 解密后的明文，str。
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
    key_length = len(self.key)
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(self.key[key_index % key_length].lower()) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            key_index += 1
        else:
            plaintext += char
    return plaintext