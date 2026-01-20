def caesar_cipher(self, plaintext, shift):
    """
    Cifra el texto plano utilizando el cifrado César.
    :param plaintext: El texto plano a encriptar, str.
    :param shift: El número de caracteres para desplazar cada carácter en el texto plano, int.
    :return: El texto cifrado, str.
    >>> e = EncryptionUtils("key")
    >>> e.caesar_cipher("abc", 1)
    'bcd'

    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determinar si es mayúscula o minúscula
            if char.isupper():
                # Desplazar dentro del rango de mayúsculas (A-Z)
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Desplazar dentro del rango de minúsculas (a-z)
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted
        else:
            # Mantener caracteres no alfabéticos sin cambios
            ciphertext += char
    return ciphertext