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
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determina se il carattere è maiuscolo o minuscolo
            if char.isupper():
                # Cripta caratteri maiuscoli
                shifted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Cripta caratteri minuscoli
                shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += shifted
        else:
            # Mantieni i caratteri non alfabetici invariati
            ciphertext += char
    return ciphertext