def caesar_decipher(self, ciphertext, shift):
    """
        使用凯撒密码解密给定的密文
        :param ciphertext: 要解密的密文，str。
        :param shift: 用于解密的位移，int。
        :return: 解密后的明文，str。
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'

        """
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext