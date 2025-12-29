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
    key_as_int = [ord(i) for i in self.key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 97)
    return plaintext