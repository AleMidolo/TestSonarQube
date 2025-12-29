def rail_fence_decipher(self, encrypted_text, rails):
    """
        使用铁路栅栏密码解密给定的密文
        :param encrypted_text: 要解密的密文，str。
        :param rails: 用于解密的栅栏数量，int。
        :return: 解密后的明文，str。
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """
    if rails <= 1:
        return encrypted_text
    fence = [['' for _ in range(len(encrypted_text))] for _ in range(rails)]
    rail = 0
    direction = 1
    for i in range(len(encrypted_text)):
        fence[rail][i] = '*'
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if fence[i][j] == '*':
                fence[i][j] = encrypted_text[index]
                index += 1
    plaintext = []
    rail = 0
    direction = 1
    for i in range(len(encrypted_text)):
        plaintext.append(fence[rail][i])
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    return ''.join(plaintext)