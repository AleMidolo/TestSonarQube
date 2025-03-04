def split(s, platform='this'):
    import re
    import sys
    import shlex

    # Detect platform if 'this' is specified
    if platform == 'this':
        platform = 1 if sys.platform != 'win32' else 0

    if platform == 1:  # POSIX
        # Use shlex for POSIX-style parsing
        return shlex.split(s)
    
    elif platform == 0:  # Windows/CMD
        # Custom parsing for Windows CMD style
        pattern = r'''(
            [^\s"']+ |           # Match unquoted words
            "[^"]*" |            # Match double-quoted strings
            '[^']*'              # Match single-quoted strings
        )'''
        
        # Find all matches using regex
        tokens = re.findall(pattern, s, re.VERBOSE)
        
        # Clean up quotes
        result = []
        for token in tokens:
            # Remove surrounding quotes if present
            if (token.startswith('"') and token.endswith('"')) or \
               (token.startswith("'") and token.endswith("'")):
                token = token[1:-1]
            result.append(token)
            
        return result
    
    else:
        raise ValueError("Invalid platform value. Use 'this', 1 (POSIX), or 0 (Windows)")