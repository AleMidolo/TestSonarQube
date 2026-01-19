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
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text