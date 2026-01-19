def vigenere_cipher(self, plaintext):
    """
    प्लेनटेक्स्ट को विजेनेरे सिफर का उपयोग करके एन्क्रिप्ट करता है।
    :param plaintext: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
    :return: ciphertext, str.
    >>> e = EncryptionUtils("key")
    >>> e.vigenere_cipher("abc")
    'kfa'

    """
    ciphertext = ""
    key = self.key
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            is_upper = char.isupper()
            char = char.lower()
            
            # Get the key character (cycling through the key)
            key_char = key[key_index % len(key)].lower()
            
            # Calculate shift amount from key character
            shift = ord(key_char) - ord('a')
            
            # Encrypt the character
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            
            # Restore case if needed
            if is_upper:
                encrypted_char = encrypted_char.upper()
            
            ciphertext += encrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters are not encrypted
            ciphertext += char
    
    return ciphertext