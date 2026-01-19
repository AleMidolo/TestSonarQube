def vigenere_decipher(self, ciphertext):
    """
    Decifra il testo cifrato fornito utilizzando il cifrario di Vigenere
    :param ciphertext: Il testo cifrato da decifrare, str.
    :return: Il testo in chiaro decifrato, str.
    >>> d = DecryptionUtils('key')
    >>> d.vigenere_decipher('ifmmp')
    'ybocl'

    """
    if not ciphertext:
        return ''
    
    key = self.key.lower()
    plaintext = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determina se il carattere è maiuscolo o minuscolo
            is_upper = char.isupper()
            char = char.lower()
            
            # Ottieni il carattere della chiave corrente
            key_char = key[key_index % len(key)]
            
            # Calcola lo shift dalla chiave
            shift = ord(key_char) - ord('a')
            
            # Decifra sottraendo lo shift
            decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            # Ripristina il caso originale
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            # Mantieni i caratteri non alfabetici invariati
            plaintext.append(char)
    
    return ''.join(plaintext)