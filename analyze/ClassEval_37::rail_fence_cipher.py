def rail_fence_cipher(self, plaintext, rails):
    """
        Encrypts the plaintext using the Rail Fence cipher.
        :param plaintext: The plaintext to encrypt, str.
        :param rails: The number of rails to use, int.
        :return: The ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
    if rails == 1:
        return plaintext
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    ciphertext = ''.join([''.join(rail) for rail in fence])
    return ciphertext