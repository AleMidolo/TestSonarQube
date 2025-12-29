def vigenere_cipher(self, plaintext):
    """
        Cripta il testo in chiaro utilizzando il cifrario di Vigenere.
        :param plaintext: Il testo in chiaro da criptare, str.
        :return: Il testo cifrato, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
    key = self.key
    key_length = len(key)
    ciphertext = ''
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext