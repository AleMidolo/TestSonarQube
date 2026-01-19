def rail_fence_cipher(self, plain_text, rails):
    """
        रेल फेंस सिफर का उपयोग करके प्लेनटेक्स्ट को एन्क्रिप्ट करता है।
        :param plain_text: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
        :return: ciphertext, str.
        >>> e = EncryptionUtils("key")
        >>> e.rail_fence_cipher("abc", 2)
        'acb'

        """
    if rails == 1:
        return plain_text
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    for char in plain_text:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction
    ciphertext = ''.join([''.join(rail) for rail in fence])
    return ciphertext