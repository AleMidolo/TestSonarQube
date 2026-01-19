def rail_fence_decipher(self, encrypted_text, rails):
    """
        Decifra il testo cifrato fornito utilizzando il cifrario Rail Fence
        :param encrypted_text: Il testo cifrato da decifrare, str.
        :param rails: Il numero di rotaie da utilizzare per la decrittazione, int.
        :return: Il testo in chiaro decifrato, str.
        >>> d = DecryptionUtils('key')
        >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
        'Hello, World!'

        """
    if rails <= 1:
        return encrypted_text
    n = len(encrypted_text)
    fence = [['\n' for _ in range(n)] for _ in range(rails)]
    dir_down = None
    row, col = (0, 0)
    for i in range(n):
        if row == 0:
            dir_down = True
        if row == rails - 1:
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
        if row == rails - 1:
            dir_down = False
        if fence[row][col] != '\n':
            result.append(fence[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return ''.join(result)