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
    result = []
    
    for char in ciphertext:
        if char.isalpha():
            # Determinar si es mayúscula o minúscula
            if char.isupper():
                # Descifrar mayúscula
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Descifrar minúscula
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            result.append(decrypted_char)
        else:
            # Mantener caracteres no alfabéticos sin cambios
            result.append(char)
    
    return ''.join(result)