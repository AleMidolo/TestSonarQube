def rail_fence_cipher(self, plain_text, rails):
    """
    使用铁路栅栏密码加密明文。
    :param plain_text: 要加密的明文，str。
    :return: 密文，str。
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
    
    # Track current rail and direction
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    # Place each character on the appropriate rail
    for char in plain_text:
        fence[rail] += char
        
        # Change direction at the top or bottom rail
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Concatenate all rails to form the cipher text
    cipher_text = ''.join(fence)
    
    return cipher_text