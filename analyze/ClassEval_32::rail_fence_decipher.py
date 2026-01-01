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
    n = len(encrypted_text)
    fence = [['' for _ in range(n)] for _ in range(rails)]
    dir_down = None
    row, col = (0, 0)
    for i in range(n):
        if row == 0:
            dir_down = True
        elif row == rails - 1:
            dir_down = False
        fence[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(rails):
        for j in range(n):
            if fence[i][j] == '*' and index < n:
                fence[i][j] = encrypted_text[index]
                index += 1
    result = []
    row, col = (0, 0)
    for i in range(n):
        if row == 0:
            dir_down = True
        elif row == rails - 1:
            dir_down = False
        if fence[row][col] != '':
            result.append(fence[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return ''.join(result)