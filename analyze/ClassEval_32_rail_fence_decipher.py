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
    fence = [['' for _ in range(len(encrypted_text))] for _ in range(rails)]
    row, col = (0, 0)
    down = False
    for i in range(len(encrypted_text)):
        if row == 0 or row == rails - 1:
            down = not down
        fence[row][col] = '*'
        col += 1
        row = row + 1 if down else row - 1
    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if fence[i][j] == '*' and index < len(encrypted_text):
                fence[i][j] = encrypted_text[index]
                index += 1
    result = []
    row, col = (0, 0)
    down = False
    for i in range(len(encrypted_text)):
        if row == 0 or row == rails - 1:
            down = not down
        result.append(fence[row][col])
        col += 1
        row = row + 1 if down else row - 1
    return ''.join(result)