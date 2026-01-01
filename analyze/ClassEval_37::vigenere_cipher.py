def vigenere_cipher(self, plaintext):
    """
        Cripta il testo in chiaro utilizzando il cifrario di Vigenere.
        :param plaintext: Il testo in chiaro da criptare, str.
        :return: Il testo cifrato, str.
        >>> e = EncryptionUtils("key")
        >>> e.vigenere_cipher("abc")
        'kfa'
        """
    ciphertext = []
    key_length = len(self.key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            key_char = self.key[i % key_length].lower()
            shift = ord(key_char) - ord('a')
            if char.isupper():
                shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext.append(shifted_char)
        else:
            ciphertext.append(char)
    return ''.join(ciphertext)