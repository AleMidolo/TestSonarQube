def palindromic_string(self):
    """
    Encuentra la subcadena palindrómica más larga en la cadena dada.
    :return: La subcadena palindrómica más larga, str.
    >>> manacher = Manacher('ababaxse')
    >>> manacher.palindromic_string()
    'ababa'

    """
    if not self.string:
        return ""
    
    # Transform string to handle even-length palindromes
    # Insert '#' between characters
    transformed = '#'.join('^{}$'.format(self.string))
    n = len(transformed)
    
    # Array to store palindrome radii
    P = [0] * n
    center = 0
    right = 0
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        # If i is within the right boundary, use previously computed values
        if i < right:
            P[i] = min(right - i, P[mirror])
        
        # Attempt to expand palindrome centered at i
        try:
            while transformed[i + P[i] + 1] == transformed[i - P[i] - 1]:
                P[i] += 1
        except IndexError:
            pass
        
        # If palindrome centered at i extends past right, adjust center and right
        if i + P[i] > right:
            center = i
            right = i + P[i]
        
        # Track the longest palindrome
        if P[i] > max_len:
            max_len = P[i]
            center_index = i
    
    # Extract the longest palindrome from original string
    start = (center_index - max_len) // 2
    return self.string[start:start + max_len]