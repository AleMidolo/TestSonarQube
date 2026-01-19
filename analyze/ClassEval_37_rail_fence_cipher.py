def rail_fence_cipher(self, plain_text, rails):
    """
    Encrypts the plaintext using the Rail Fence cipher.
    :param plaintext: The plaintext to encrypt, str.
    :return: The ciphertext, str.
    >>> e = EncryptionUtils("key")
    >>> e.rail_fence_cipher("abc", 2)
    'acb'

    """
    if rails <= 1 or len(plain_text) <= 1:
        return plain_text
    
    # Create a list of empty strings for each rail
    fence = [[] for _ in range(rails)]
    
    # Direction: 1 for down, -1 for up
    rail = 0
    direction = 1
    
    # Place each character on the appropriate rail
    for char in plain_text:
        fence[rail].append(char)
        
        # Change direction at the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Read off the rails to create the ciphertext
    cipher_text = ''.join([''.join(rail) for rail in fence])
    
    return cipher_text