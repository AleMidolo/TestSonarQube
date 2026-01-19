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
    
    key = self.key if hasattr(self, 'key') else self
    ciphertext = []
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the key character (循环使用key)
            key_char = key[key_index % len(key)].lower()
            
            # Calculate shift amount (a=0, b=1, ..., z=25)
            shift = ord(key_char) - ord('a')
            
            # Encrypt the character
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            # Restore case if needed
            if is_upper:
                encrypted_char = encrypted_char.upper()
            
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters are not encrypted
            ciphertext.append(char)
    
    return ''.join(ciphertext)