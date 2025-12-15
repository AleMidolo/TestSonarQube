def rail_fence_cipher(self, plain_text, rails):
    """
    使用铁路栅栏密码加密明文。
    :param plain_text: 要加密的明文，str。
    :return: 密文，str。
    >>> e = EncryptionUtils("key")
    >>> e.rail_fence_cipher("abc", 2)
    'acb'
    """
    
    if rails <= 0:
        return ""
    
    rail = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0

    for char in plain_text:
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    ciphertext = ""
    for r in rail:
        for c in r:
            if c != '\n':
                ciphertext += c

    return ciphertext