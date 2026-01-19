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
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the key character
            key_char = key[key_index % key_length]
            
            # Decrypt: shift back by key character value
            shift = ord(key_char) - ord('a')
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Restore case
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)
    
    return ''.join(plaintext)