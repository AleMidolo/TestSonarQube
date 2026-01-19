def vigenere_decipher(self, ciphertext):
    """
    Decifra il testo cifrato fornito utilizzando il cifrario di Vigenere
    :param ciphertext: Il testo cifrato da decifrare, str.
    :return: Il testo in chiaro decifrato, str.
    >>> d = DecryptionUtils('key')
    >>> d.vigenere_decipher('ifmmp')
    'ybocl'

    """
    if not hasattr(self, 'key'):
        raise AttributeError("Object must have a 'key' attribute")
    
    key = self.key
    plaintext = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the key character (cycling through the key)
            key_char = key[key_index % len(key)].lower()
            
            # Decrypt: shift back by the key character's position
            char_pos = ord(char) - ord('a')
            key_pos = ord(key_char) - ord('a')
            decrypted_pos = (char_pos - key_pos) % 26
            decrypted_char = chr(decrypted_pos + ord('a'))
            
            # Restore case
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            # Non-alphabetic characters are added as-is
            plaintext.append(char)
    
    return ''.join(plaintext)