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
    if rails == 1:
        return encrypted_text
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    pattern = []
    for i in range(len(encrypted_text)):
        pattern.append(rail)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    sorted_pattern = sorted(range(len(pattern)), key=lambda i: pattern[i])
    for i, pos in enumerate(sorted_pattern):
        fence[pattern[pos]].append(encrypted_text[i])
    result = []
    rail = 0
    direction = 1
    rail_indices = [0] * rails
    for _ in range(len(encrypted_text)):
        result.append(fence[rail][rail_indices[rail]])
        rail_indices[rail] += 1
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    return ''.join(result)