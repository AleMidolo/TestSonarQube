def vigenere_decipher(self, ciphertext):
    """
    दिए गए ciphertext को Vigenere cipher का उपयोग करके डिकोड करता है
    :param ciphertext: डिकोड करने के लिए ciphertext, str.
    :return: डिकोड किया गया plaintext, str.
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
            
            # Decrypt: shift back by the key character's position
            char_pos = ord(char) - ord('a')
            key_pos = ord(key_char) - ord('a')
            decrypted_pos = (char_pos - key_pos) % 26
            decrypted_char = chr(decrypted_pos + ord('a'))
            
            # Restore case
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)