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
    rail = [['\n' for i in range(len(encrypted_text))] for j in range(rails)]
    dir_down = None
    row, col = (0, 0)
    for char in encrypted_text:
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(rails):
        for j in range(len(encrypted_text)):
            if rail[i][j] == '*' and index < len(encrypted_text):
                rail[i][j] = encrypted_text[index]
                index += 1
    result = []
    row, col = (0, 0)
    for char in encrypted_text:
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return ''.join(result)