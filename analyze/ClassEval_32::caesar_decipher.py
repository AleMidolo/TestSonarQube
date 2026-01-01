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
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext