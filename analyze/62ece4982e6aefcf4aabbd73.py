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
        pattern = r'''(?:"[^"]*"|'[^']*'|\S+)'''

    # Find all matches
    tokens = re.findall(pattern, s)

    # Remove surrounding quotes and unescape internal quotes
    result = []
    for token in tokens:
        if (token.startswith('"') and token.endswith('"')) or \
           (token.startswith("'") and token.endswith("'")):
            # Remove surrounding quotes
            token = token[1:-1]
            # Unescape internal quotes
            token = token.replace('\\"', '"').replace("\\'", "'")
        result.append(token)

    return result