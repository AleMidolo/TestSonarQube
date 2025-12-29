def caesar_cipher(self, plaintext, shift):
    """
        Cripta il testo in chiaro utilizzando il cifrario di Cesare.
        :param plaintext: Il testo in chiaro da criptare, str.
        :param shift: Il numero di caratteri da spostare per ogni carattere nel testo in chiaro, int.
        :return: Il testo cifrato, str.
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