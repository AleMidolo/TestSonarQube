def split(s, platform='this'):
    import re
    import sys
    
    # Determine platform
    if platform == 'this':
        platform = 1 if sys.platform != 'win32' else 0
        
    if platform == 1:  # POSIX style
        # Match either a non-whitespace sequence, or a quoted string with possible escaped quotes
        pattern = r'''(?:[^\s"']|"(?:\\.|[^"])*"|'(?:\\.|[^'])*')+'''
        
        # Split and handle quotes/escapes
        tokens = re.findall(pattern, s)
        result = []
        for token in tokens:
            if (token.startswith('"') and token.endswith('"')) or \
               (token.startswith("'") and token.endswith("'")):
                # Remove quotes and unescape
                token = token[1:-1].replace('\\"', '"').replace("\\'", "'")
            result.append(token)
            
    else:  # Windows/CMD style
        # Match either a non-whitespace sequence, or a quoted string
        pattern = r'''(?:[^\s"]|"[^"]*")+'''
        
        # Split and handle quotes
        tokens = re.findall(pattern, s)
        result = []
        for token in tokens:
            if token.startswith('"') and token.endswith('"'):
                # Remove quotes but don't unescape
                token = token[1:-1]
            result.append(token)
            
    return result