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
    if rails <= 1 or len(encrypted_text) <= 1:
        return encrypted_text
    
    # Create a matrix to mark positions
    fence = [[None for _ in range(len(encrypted_text))] for _ in range(rails)]
    
    # Mark the positions in zigzag pattern
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    for col in range(len(encrypted_text)):
        fence[rail][col] = '*'
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Fill the fence with encrypted text characters
    index = 0
    for row in range(rails):
        for col in range(len(encrypted_text)):
            if fence[row][col] == '*':
                fence[row][col] = encrypted_text[index]
                index += 1
    
    # Read the fence in zigzag pattern to get decrypted text
    result = []
    rail = 0
    direction = 1
    
    for col in range(len(encrypted_text)):
        result.append(fence[rail][col])
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    return ''.join(result)