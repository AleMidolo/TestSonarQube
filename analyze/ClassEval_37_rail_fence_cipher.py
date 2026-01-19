def rail_fence_cipher(self, plain_text, rails):
    """
    रेल फेंस सिफर का उपयोग करके प्लेनटेक्स्ट को एन्क्रिप्ट करता है।
    :param plain_text: एन्क्रिप्ट करने के लिए प्लेनटेक्स्ट, str.
    :return: ciphertext, str.
    >>> e = EncryptionUtils("key")
    >>> e.rail_fence_cipher("abc", 2)
    'acb'

    """
    if rails <= 0 or len(plain_text) == 0:
        return plain_text
    
    if rails == 1:
        return plain_text
    
    # Create a list of strings for each rail
    fence = [[] for _ in range(rails)]
    
    # Direction: 0 = down, 1 = up
    rail = 0
    direction = 1  # Start going down
    
    # Place each character on the appropriate rail
    for char in plain_text:
        fence[rail].append(char)
        
        # Change direction at the top or bottom rail
        if rail == 0:
            direction = 1  # Go down
        elif rail == rails - 1:
            direction = -1  # Go up
        
        rail += direction
    
    # Read off the rails to create the ciphertext
    ciphertext = ''.join([''.join(rail_chars) for rail_chars in fence])
    
    return ciphertext