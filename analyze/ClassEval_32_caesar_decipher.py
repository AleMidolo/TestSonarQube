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
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text