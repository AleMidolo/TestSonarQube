def rail_fence_cipher(self, plain_text, rails):
    """
        Cifra el texto plano utilizando el cifrado Rail Fence.
        :param plain_text: El texto plano a encriptar, str.
        :return: El texto cifrado, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
    rail = [['\n' for i in range(len(plain_text))] for j in range(rails)]
    dir_down = None
    row, col = (0, 0)
    for char in plain_text:
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        rail[row][col] = char
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(rails):
        for j in range(len(plain_text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return ''.join(result)