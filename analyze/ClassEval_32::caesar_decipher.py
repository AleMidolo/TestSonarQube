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