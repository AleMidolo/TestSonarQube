def rail_fence_cipher(self, plain_text, rails):
    """
        使用铁路栅栏密码加密明文。
        :param plain_text: 要加密的明文，str。
        :param rails: 使用的栅栏数量，int。
        :return: 密文，str。
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'
        """
    if rails <= 0:
        return ''
    rail = ['' for _ in range(rails)]
    direction_down = False
    row = 0
    for char in plain_text:
        rail[row] += char
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        row += 1 if direction_down else -1
    return ''.join(rail)