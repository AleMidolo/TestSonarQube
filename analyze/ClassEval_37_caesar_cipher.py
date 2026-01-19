def caesar_cipher(self, plaintext, shift):
    """
    Encrypts the plaintext using the Caesar cipher.
    :param plaintext: The plaintext to encrypt, str.
    :param shift: The number of characters to shift each character in the plaintext, int.
    :return: The ciphertext, str.
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