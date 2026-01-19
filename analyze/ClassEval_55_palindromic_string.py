def palindromic_string(self):
    """
    在给定的字符串中找到最长的回文子串。
    :return: 最长的回文子串，str。
    >>> manacher = Manacher('ababaxse')
    >>> manacher.palindromic_string()
    'ababa'

    """
    if not self.s:
        return ""
    
    # Transform string to avoid even/odd length issues
    # Insert '#' between characters
    t = '#'.join('^{}$'.format(self.s))
    n = len(t)
    p = [0] * n  # Array to store radius of palindrome at each position
    center = 0  # Center of the rightmost palindrome
    right = 0   # Right boundary of the rightmost palindrome
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        # If i is within right boundary, we can use previously computed values
        if i < right:
            p[i] = min(right - i, p[mirror])
        
        # Attempt to expand palindrome centered at i
        try:
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1
        except IndexError:
            pass
        
        # If palindrome centered at i extends past right, adjust center and right
        if i + p[i] > right:
            center = i
            right = i + p[i]
        
        # Track the longest palindrome
        if p[i] > max_len:
            max_len = p[i]
            center_index = i
    
    # Extract the longest palindrome from original string
    start = (center_index - max_len) // 2
    return self.s[start:start + max_len]