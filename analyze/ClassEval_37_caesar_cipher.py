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
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    return ciphertext