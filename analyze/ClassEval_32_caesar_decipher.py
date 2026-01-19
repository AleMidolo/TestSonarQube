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
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text