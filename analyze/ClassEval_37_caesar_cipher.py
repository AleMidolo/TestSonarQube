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
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift within uppercase letters (A-Z)
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift within lowercase letters (a-z)
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    return ciphertext