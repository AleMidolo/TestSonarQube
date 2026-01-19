def vigenere_decipher(self, ciphertext):
    """
    Deciphers the given ciphertext using the Vigenere cipher
    :param ciphertext: The ciphertext to decipher,str.
    :return: The deciphered plaintext,str.
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
            
            # Decipher by subtracting the shift
            deciphered_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Restore case if needed
            if is_upper:
                deciphered_char = deciphered_char.upper()
            
            plaintext.append(deciphered_char)
            key_index += 1
        else:
            # Non-alphabetic characters are added as-is
            plaintext.append(char)
    
    return ''.join(plaintext)