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
            
            # Ottieni il valore numerico del carattere (a=0, b=1, ..., z=25)
            char_value = ord(char) - ord('a')
            
            # Ottieni il valore della chiave corrente
            key_char = key[key_index % len(key)]
            key_value = ord(key_char) - ord('a')
            
            # Decifra sottraendo il valore della chiave
            decrypted_value = (char_value - key_value) % 26
            
            # Converti di nuovo in carattere
            decrypted_char = chr(decrypted_value + ord('a'))
            
            # Ripristina maiuscolo se necessario
            if is_upper:
                decrypted_char = decrypted_char.upper()
            
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            # Mantieni i caratteri non alfabetici invariati
            plaintext.append(char)
    
    return ''.join(plaintext)