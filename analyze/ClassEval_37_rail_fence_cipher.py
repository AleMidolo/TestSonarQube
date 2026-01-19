def rail_fence_cipher(self, plain_text, rails):
    """
    Cifra el texto plano utilizando el cifrado Rail Fence.
    :param plain_text: El texto plano a encriptar, str.
    :return: El texto cifrado, str.
    >>> e = EncryptionUtils("key")
    >>> e.rail_fence_cipher("abc", 2)
    'acb'

    """
    if rails <= 0 or len(plain_text) == 0:
        return plain_text
    
    if rails == 1:
        return plain_text
    
    # Create the rail fence pattern
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    # Place characters in the fence pattern
    for char in plain_text:
        fence[rail].append(char)
        
        # Change direction at the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Read off the cipher text row by row
    cipher_text = ''.join([''.join(row) for row in fence])
    
    return cipher_text