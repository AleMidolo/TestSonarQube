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
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text