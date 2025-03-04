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
        # Match single or double quoted strings, or unquoted sequences
        pattern = r'''(?:[^\s"']+|"[^"]*"|'[^']*')+'''
        matches = re.findall(pattern, s)
        # Remove surrounding quotes if present
        return [m.strip('"\'') for m in matches]
        
    elif platform == 0:  # Windows/CMD
        # Windows command line splitting rules:
        # - Backslash is literal unless followed by quote
        # - Quotes must be paired
        # - Spaces outside quotes separate arguments
        result = []
        current = []
        in_quotes = False
        i = 0
        
        while i < len(s):
            if s[i] == '"':
                if in_quotes and i + 1 < len(s) and s[i + 1] == '"':
                    current.append('"')
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif s[i] == ' ' and not in_quotes:
                if current:
                    result.append(''.join(current))
                    current = []
            else:
                current.append(s[i])
            i += 1
            
        if current:
            result.append(''.join(current))
            
        return result
        
    else:
        raise ValueError("Unsupported platform value")