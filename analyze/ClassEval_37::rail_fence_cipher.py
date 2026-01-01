def rail_fence_cipher(self, plain_text, rails):
    """
        使用铁路栅栏密码加密明文。
        :param plain_text: 要加密的明文，str。
        :return: 密文，str。
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