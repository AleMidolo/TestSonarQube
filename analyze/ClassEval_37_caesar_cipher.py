def caesar_cipher(self, plaintext, shift):
    """
    使用凯撒密码加密明文。
    :param plaintext: 要加密的明文，str。
    :param shift: 每个字符在明文中移动的字符数，int。
    :return: 密文，str。
    >>> e = EncryptionUtils("key")
    >>> e.caesar_cipher("abc", 1)
    'bcd'

    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # 判断是大写还是小写
            if char.isupper():
                # 大写字母处理
                shifted = (ord(char) - ord('A') + shift) % 26
                ciphertext += chr(shifted + ord('A'))
            else:
                # 小写字母处理
                shifted = (ord(char) - ord('a') + shift) % 26
                ciphertext += chr(shifted + ord('a'))
        else:
            # 非字母字符保持不变
            ciphertext += char
    return ciphertext