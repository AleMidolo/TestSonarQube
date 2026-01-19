def vigenere_decipher(self, ciphertext):
    """
        दिए गए ciphertext को Vigenere cipher का उपयोग करके डिकोड करता है
        :param ciphertext: डिकोड करने के लिए ciphertext, str.
        :return: डिकोड किया गया plaintext, str.
        >>> d = DecryptionUtils('key')
        >>> d.vigenere_decipher('ifmmp')
        'ybocl'
        """
    key = self.key
    key_length = len(key)
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length].lower()) - ord('a')
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            key_index += 1
        else:
            plaintext += char
    return plaintext