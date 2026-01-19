def caesar_decipher(self, ciphertext, shift):
    """
    Deciphers the given ciphertext using the Caesar cipher
    :param ciphertext: The ciphertext to decipher,str.
    :param shift: The shift to use for decryption,int.
    :return: The deciphered plaintext,str.
    >>> d = DecryptionUtils('key')
    >>> d.caesar_decipher('ifmmp', 1)
    'hello'

    """
    plaintext = []
    for char in ciphertext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift back by the given amount for uppercase
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Shift back by the given amount for lowercase
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext.append(decrypted_char)
        else:
            # Non-alphabetic characters remain unchanged
            plaintext.append(char)
    
    return ''.join(plaintext)