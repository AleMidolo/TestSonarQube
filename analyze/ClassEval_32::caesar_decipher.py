def caesar_decipher(self, ciphertext, shift):
    """
        Decifra il testo cifrato fornito utilizzando il cifrario di Cesare
        :param ciphertext: Il testo cifrato da decifrare, str.
        :param shift: Lo spostamento da utilizzare per la decrittazione, int.
        :return: Il testo in chiaro decifrato, str.
        >>> d = DecryptionUtils('key')
        >>> d.caesar_decipher('ifmmp', 1)
        'hello'

        """
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            plaintext += chr((ord(char) - base - shift) % 26 + base)
        else:
            plaintext += char
    return plaintext