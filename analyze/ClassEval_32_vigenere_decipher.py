def vigenere_decipher(self, ciphertext):
    """
    使用维吉尼亚密码解密给定的密文
    :param ciphertext: 要解密的密文，str。
    :return: 解密后的明文，str。
    >>> d = DecryptionUtils('key')
    >>> d.vigenere_decipher('ifmmp')
    'ybocl'

    """
    plaintext = []
    key = self.key.lower()
    key_length = len(key)
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the shift value from the key
            shift = ord(key[key_index % key_length]) - ord('a')
            
            # Decrypt by shifting backwards
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Restore case
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters are not encrypted
            plaintext.append(char)
    
    return ''.join(plaintext)