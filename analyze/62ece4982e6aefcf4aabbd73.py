def split(s, platform='this'):
    import re
    import sys
    
    # Determine platform
    if platform == 'this':
        platform = 0 if sys.platform.startswith('win') else 1
    
    if platform == 1:  # POSIX style
        # Handle escaped quotes and spaces
        s = s.replace('\\"', '\x00').replace("\\'", '\x01')
        
        # Split on spaces while preserving quoted strings
        pattern = r'''(?:[^\s"'\\]|\\.|"(?:\\.|[^"])*"|'(?:\\.|[^'])*')+'''
        tokens = re.findall(pattern, s)
        
        # Clean up tokens
        result = []
        for token in tokens:
            # Remove enclosing quotes if present
            if (token.startswith('"') and token.endswith('"')) or \
               (token.startswith("'") and token.endswith("'")):
                token = token[1:-1]
            
            # Restore escaped characters
            token = token.replace('\x00', '"').replace('\x01', "'")
            token = token.replace('\\\\', '\\').replace('\\"', '"').replace("\\'", "'")
            result.append(token)
            
        return result
        
    elif platform == 0:  # Windows/CMD style
        # Handle escaped quotes
        s = s.replace('\\"', '\x00')
        
        # Split on spaces while preserving quoted strings
        pattern = r'''(?:[^\s"]|"(?:\\.|[^"])*")+'''
        tokens = re.findall(pattern, s)
        
        # Clean up tokens
        result = []
        for token in tokens:
            # Remove enclosing quotes if present
            if token.startswith('"') and token.endswith('"'):
                token = token[1:-1]
                
            # Restore escaped characters    
            token = token.replace('\x00', '"').replace('\\\\', '\\')
            result.append(token)
            
        return result
        
    else:
        raise ValueError("Invalid platform value")