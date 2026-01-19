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
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # 判断是大写还是小写
            if char.isupper():
                # 解密：向后移动shift位，相当于向前移动shift位
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # 解密：向后移动shift位，相当于向前移动shift位
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            # 非字母字符保持不变
            plaintext += char
    return plaintext