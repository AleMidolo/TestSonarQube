def rail_fence_cipher(self, plain_text, rails):
    """
    Cripta il testo in chiaro utilizzando il cifrario Rail Fence.
    :param plain_text: Il testo in chiaro da criptare, str.
    :return: Il testo cifrato, str.
    >>> e = EncryptionUtils("key")
    >>> e.rail_fence_cipher("abc", 2)
    'acb'

    """
    if rails <= 0 or len(plain_text) == 0:
        return plain_text
    
    if rails == 1:
        return plain_text
    
    # Create a list of strings for each rail
    fence = ['' for _ in range(rails)]
    
    # Direction: 0 = down, 1 = up
    rail = 0
    direction = 0  # Start going down
    
    # Place each character on the appropriate rail
    for char in plain_text:
        fence[rail] += char
        
        # Change direction at the top or bottom rail
        if rail == 0:
            direction = 0  # Go down
        elif rail == rails - 1:
            direction = 1  # Go up
        
        # Move to next rail
        if direction == 0:
            rail += 1
        else:
            rail -= 1
    
    # Concatenate all rails to get the cipher text
    cipher_text = ''.join(fence)
    
    return cipher_text