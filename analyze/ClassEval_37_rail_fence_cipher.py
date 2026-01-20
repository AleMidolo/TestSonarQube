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
    
    # Create a list of strings for each rail
    fence = [''] * rails
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    # Place each character on the appropriate rail
    for char in plain_text:
        fence[rail] += char
        rail += direction
        
        # Change direction at the top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    # Concatenate all rails to get the cipher text
    cipher_text = ''.join(fence)
    
    return cipher_text