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
            
            # Convert characters to numbers (a=0, b=1, ..., z=25)
            char_num = ord(char) - ord('a')
            key_num = ord(key_char) - ord('a')
            
            # Decipher: subtract key from ciphertext (mod 26)
            plain_num = (char_num - key_num) % 26
            
            # Convert back to character
            plain_char = chr(plain_num + ord('a'))
            
            # Restore original case
            if is_upper:
                plain_char = plain_char.upper()
            
            plaintext.append(plain_char)
        else:
            # Non-alphabetic characters remain unchanged
            plaintext.append(char)
    
    return ''.join(plaintext)