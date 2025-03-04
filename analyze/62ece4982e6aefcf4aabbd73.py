def split(s, platform='this'):
    import re
    import sys

    # Determine platform if auto-detect
    if platform == 'this':
        platform = 1 if sys.platform != 'win32' else 0

    if platform == 1:  # POSIX style
        # Match either:
        # - Quoted string with escaped quotes allowed
        # - Unquoted string with no whitespace
        pattern = r'''(?:[^\s'"]*(?:'[^']*'|"[^"]*")[^\s'"]*)+|[^\s'"]+'''
        
    else:  # Windows/CMD style
        # Match either:
        # - Quoted string with escaped quotes allowed
        # - Unquoted string with no whitespace
        pattern = r'''"[^"]*"|'[^']*'|\S+'''

    # Find all matches
    tokens = re.findall(pattern, s)

    # Post-process tokens
    result = []
    for token in tokens:
        # Remove surrounding quotes if present
        if (token.startswith('"') and token.endswith('"')) or \
           (token.startswith("'") and token.endswith("'")):
            token = token[1:-1]
            
        # Handle escaped quotes
        if platform == 1:  # POSIX
            token = token.replace('\\"', '"').replace("\\'", "'")
        else:  # Windows
            token = token.replace('""', '"')
            
        result.append(token)

    return result