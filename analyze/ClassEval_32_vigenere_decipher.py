def vigenere_decipher(self, ciphertext):
    """
        Deciphers the given ciphertext using the Vigenere cipher
        :param ciphertext: The ciphertext to decipher,str.
        :return: The deciphered plaintext,str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
    key_length = len(self.key)
    plaintext = []
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(self.key[key_index % key_length].lower()) - ord('a')
            if char.isupper():
                plain_char = chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plain_char = chr((ord(char) - shift - 97) % 26 + 97)
            plaintext.append(plain_char)
            key_index += 1
        else:
            plaintext.append(char)
    return ''.join(plaintext)