def rail_fence_decipher(self, encrypted_text, rails):
    """
    दिए गए ciphertext को Rail Fence cipher का उपयोग करके डिकोड करता है
    :param encrypted_text: डिकोड करने के लिए ciphertext, str.
    :param rails: डिक्रिप्शन के लिए उपयोग करने के लिए रेल की संख्या, int.
    :return: डिकोड किया गया plaintext, str.
    >>> d = DecryptionUtils('key')
    >>> d.rail_fence_decipher('Hoo!el,Wrdl l', 3)
    'Hello, World!'
    """
    rail = [['\n' for i in range(len(encrypted_text))] for j in range(rails)]
    dir_down = None
    row, col = (0, 0)
    for i in range(len(encrypted_text)):
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
    for i in range(len(encrypted_text)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return ''.join(result)