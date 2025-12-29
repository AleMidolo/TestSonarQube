def rail_fence_cipher(self, plain_text, rails):
    """
        Cripta il testo in chiaro utilizzando il cifrario Rail Fence.
        :param plain_text: Il testo in chiaro da criptare, str.
        :return: Il testo cifrato, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
    if rails <= 1:
        return plain_text
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in plain_text:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction *= -1
    ciphertext = ''.join([''.join(rail) for rail in fence])
    return ciphertext