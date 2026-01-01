def rail_fence_decipher(self, encrypted_text, rails):
    """
        Descifra el texto cifrado dado utilizando el cifrado Rail Fence
        :param encrypted_text: El texto cifrado a descifrar, str.
        :param rails: El número de rieles a utilizar para la descifrado, int.
        :return: El texto plano descifrado, str.
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
    result = []
    rail = 0
    direction = 1
    for i in range(len(encrypted_text)):
        result.append(fence[rail][i])
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    return ''.join(result)