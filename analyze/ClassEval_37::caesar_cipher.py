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
            shift_amount = shift % 26
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text