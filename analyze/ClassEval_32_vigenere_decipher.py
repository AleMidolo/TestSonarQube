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
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the key character for this position
            key_char = key[i % key_length]
            
            # Calculate the shift value from the key character
            shift = ord(key_char) - ord('a')
            
            # Decipher by subtracting the shift
            deciphered_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Restore original case
            if is_upper:
                deciphered_char = deciphered_char.upper()
            
            plaintext.append(deciphered_char)
        else:
            # Non-alphabetic characters remain unchanged
            plaintext.append(char)
    
    return ''.join(plaintext)