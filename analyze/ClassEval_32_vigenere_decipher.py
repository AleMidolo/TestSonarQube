def vigenere_decipher(self, ciphertext):
    """
    Descifra el texto cifrado dado utilizando el cifrado de Vigenere
    :param ciphertext: El texto cifrado a descifrar, str.
    :return: El texto plano descifrado, str.
    >>> d = DecryptionUtils('key')
    >>> d.vigenere_decipher('ifmmp')
    'ybocl'

    """
    if not ciphertext:
        return ''
    
    key = self.key.lower()
    result = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the shift value from the key
            shift = ord(key[key_index % len(key)]) - ord('a')
            
            # Decrypt by subtracting the shift
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Restore case
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            result.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters are not decrypted
            result.append(char)
    
    return ''.join(result)