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
    
    # Assuming self.key exists as an instance variable
    key = self.key.lower()
    plaintext = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the shift value from the key
            shift = ord(key[key_index % len(key)]) - ord('a')
            
            # Decrypt by subtracting the shift (reverse of encryption)
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Restore case
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters are not decrypted
            plaintext.append(char)
    
    return ''.join(plaintext)