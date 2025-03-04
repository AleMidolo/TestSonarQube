def split(s, platform='this'):
    import re
    import sys
    
    # Determine platform
    if platform == 'this':
        platform = 0 if sys.platform.startswith('win') else 1
    
    if platform == 1:  # POSIX style
        # Match either:
        # - Quoted string with escaped quotes allowed
        # - Unquoted string with no whitespace
        pattern = r'''(?:[^\s'"]*(?:'[^']*'|"[^"]*")[^\s'"]*)+|[^\s'"]+'''
        
        # Split and clean up quotes
        parts = re.findall(pattern, s)
        result = []
        for part in parts:
            # Remove outer quotes if present
            if (part.startswith('"') and part.endswith('"')) or \
               (part.startswith("'") and part.endswith("'")):
                part = part[1:-1]
            # Unescape inner quotes
            part = part.replace('\\"', '"').replace("\\'", "'")
            result.append(part)
            
    else:  # Windows/CMD style
        # Match either:
        # - Quoted string (no escaped quotes in Windows)
        # - Unquoted string with no whitespace
        pattern = r'"[^"]*"|[^\s"]+'
        
        # Split and clean up quotes
        parts = re.findall(pattern, s)
        result = []
        for part in parts:
            # Remove outer quotes if present
            if part.startswith('"') and part.endswith('"'):
                part = part[1:-1]
            result.append(part)
            
    return result