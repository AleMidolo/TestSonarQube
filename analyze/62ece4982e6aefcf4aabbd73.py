def split(s, platform='this'):
    """
    Multi-platform variant of shlex.split() for command-line splitting.
    For use with subprocess, for argv injection etc. Using fast REGEX.
    
    platform: 'this' = auto from current platform;
              1 = POSIX;
              0 = Windows/CMD
              (other values reserved)
    """
    import re
    import sys
    
    if platform == 'this':
        platform = 1 if sys.platform != 'win32' else 0
        
    if platform == 1:  # POSIX
        # Match either a non-whitespace sequence, or a quoted string
        pattern = r'''(?:[^\s"']+|"[^"]*"|'[^']*')+'''
        
        # Split and handle quotes
        tokens = re.findall(pattern, s)
        result = []
        for token in tokens:
            # Remove surrounding quotes and unescape
            if (token.startswith('"') and token.endswith('"')) or \
               (token.startswith("'") and token.endswith("'")):
                token = token[1:-1]
            result.append(token)
            
    else:  # Windows/CMD
        # Windows splits on spaces unless quoted
        pattern = r'''("[^"]*"|[^\s"]+)'''
        
        # Split and handle quotes
        tokens = re.findall(pattern, s)
        result = []
        for token in tokens:
            # Remove surrounding quotes but don't unescape
            if token.startswith('"') and token.endswith('"'):
                token = token[1:-1]
            result.append(token)
            
    return result