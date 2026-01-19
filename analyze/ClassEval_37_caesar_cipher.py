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
    encrypted_text = ''
    for char in plaintext:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text