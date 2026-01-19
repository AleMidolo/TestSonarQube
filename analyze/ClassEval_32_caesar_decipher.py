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
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Determina se il carattere è maiuscolo o minuscolo
            if char.isupper():
                # Decifra carattere maiuscolo
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Decifra carattere minuscolo
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            # Mantieni i caratteri non alfabetici invariati
            plaintext += char
    return plaintext