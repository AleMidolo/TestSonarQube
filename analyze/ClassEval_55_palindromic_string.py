def palindromic_string(self):
    """
    Trova la sottostringa palindromica più lunga nella stringa fornita.
    :return: La sottostringa palindromica più lunga, str.
    >>> manacher = Manacher('ababaxse')
    >>> manacher.palindromic_string()
    'ababa'

    """
    if not self.string or len(self.string) == 0:
        return ""
    
    # Transform string to handle even-length palindromes
    # Insert '#' between characters
    transformed = '#'.join('^{}$'.format(self.string))
    n = len(transformed)
    
    # Array to store palindrome radii
    p = [0] * n
    center = 0
    right = 0
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        # If i is within right boundary, use previously computed values
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        # Attempt to expand palindrome centered at i
        try:
            while transformed[i + (1 + p[i])] == transformed[i - (1 + p[i])]:
                p[i] += 1
        except IndexError:
            pass
        
        # If palindrome centered at i extends past right, adjust center
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        # Track the longest palindrome
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    
    # Extract the longest palindrome from original string
    start = (center_index - max_len) // 2
    return self.string[start:start + max_len]