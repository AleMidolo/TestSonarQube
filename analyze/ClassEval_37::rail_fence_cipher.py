def rail_fence_cipher(self, plain_text, rails):
    """
    रेल फेंस सिफर का उपयोग करके प्लेनटेक्स्ट को एन्क्रिप्ट करता है।
    :param plain_text: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
    :return: ciphertext, str.
    >>> e = EncryptionUtils("key")
    >>> e.rail_fence_cipher("abc", 2)
    'acb'
    """
    if rails <= 0:
        return ''
    rail = [['\n' for _ in range(len(plain_text))] for _ in range(rails)]
    direction_down = False
    row, col = (0, 0)
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
    ciphertext = ''
    for r in rail:
        for c in r:
            if c != '\n':
                ciphertext += c
    return ciphertext