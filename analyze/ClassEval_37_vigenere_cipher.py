def vigenere_cipher(self, plaintext):
    """
    使用维吉尼亚密码加密明文。
    :param plaintext: 要加密的明文，str。
    :return: 密文，str。
    >>> e = EncryptionUtils("key")
    >>> e.vigenere_cipher("abc")
    'kfa'

    """
    if not plaintext:
        return ""
    
    # Assume self.key is the encryption key
    key = self.key.lower()
    plaintext_lower = plaintext.lower()
    ciphertext = []
    key_index = 0
    
    for char in plaintext_lower:
        if char.isalpha():
            # Get the shift value from the key
            shift = ord(key[key_index % len(key)]) - ord('a')
            # Encrypt the character
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters are not encrypted
            ciphertext.append(char)
    
    return ''.join(ciphertext)