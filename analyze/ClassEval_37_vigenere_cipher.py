def vigenere_cipher(self, plaintext):
    """
    Cripta il testo in chiaro utilizzando il cifrario di Vigenere.
    :param plaintext: Il testo in chiaro da criptare, str.
    :return: Il testo cifrato, str.
    >>> e = EncryptionUtils("key")
    >>> e.vigenere_cipher("abc")
    'kfa'

    """
    if not plaintext:
        return ""
    
    # Assume self.key exists as an instance variable
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