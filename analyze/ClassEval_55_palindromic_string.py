def palindromic_string(self):
    """
    Finds the longest palindromic substring in the given string.
    :return: The longest palindromic substring, str.
    >>> manacher = Manacher('ababaxse')
    >>> manacher.palindromic_string()
    'ababa'

    """
    if not self.string:
        return ""
    
    # Transform string to avoid even/odd length issues
    # Insert '#' between characters: "abc" -> "#a#b#c#"
    transformed = '#'.join('^{}$'.format(self.string))
    n = len(transformed)
    
    # Array to store the radius of palindrome at each position
    P = [0] * n
    center = 0  # Center of the rightmost palindrome
    right = 0   # Right boundary of the rightmost palindrome
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        # If i is within the right boundary, we can use previously computed values
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
    
    # Extract the longest palindromic substring from original string
    start = (center_index - max_len) // 2
    return self.string[start:start + max_len]