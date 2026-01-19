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
    fence = [['' for _ in range(n)] for _ in range(rails)]
    row, col, down = (0, 0, False)
    for i in range(n):
        fence[row][col] = '*'
        col += 1
        if row == 0 or row == rails - 1:
            down = not down
        row += 1 if down else -1
    index = 0
    for i in range(rails):
        for j in range(n):
            if fence[i][j] == '*':
                fence[i][j] = encrypted_text[index]
                index += 1
    result = []
    row, col, down = (0, 0, False)
    for i in range(n):
        result.append(fence[row][col])
        col += 1
        if row == 0 or row == rails - 1:
            down = not down
        row += 1 if down else -1
    return ''.join(result)