def caesar_decipher(self, ciphertext, shift):
    """
        Descifra el texto cifrado dado utilizando el cifrado César.
        :param ciphertext: El texto cifrado a descifrar, str.
        :param shift: El desplazamiento a utilizar para la descifrado, int.
        :return: El texto plano descifrado, str.
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